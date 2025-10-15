from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import sys
import random
import math
import time
import json
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from typing import Optional

# Добавляем путь к функциям
sys.path.append(os.path.join(os.path.dirname(__file__), 'func'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'configs'))

#TARIFS
TON_MIN = 500
TON_MAX = 10000
ETH_MIN = 10000
ETH_MAX = 100000
USDT_MIN = 100000
USDT_MAX = 10000000

# Ежедневная прибыль в процентах
STAKE_TON_PROFIT = 1.7
STAKE_ETH_PROFIT = 2.1
STAKE_USDT_PROFIT = 2.7

# Интервал обновления прибыли (10 секунд)
PROFIT_UPDATE_INTERVAL = 10.0

# Конфигурация тарифов
# ВАЖНО: balance_threshold теперь означает минимальный СТЕЙКОВЫЙ баланс для тарифа
TARIFF_CONFIG = {
    'TON': {
        'name': 'TON',
        'icon': '/icon/ton.svg',
        'min_amount': TON_MIN,
        'max_amount': TON_MAX,
        'daily_profit': STAKE_TON_PROFIT,
        'balance_threshold': 0  # Базовый тариф - доступен всегда
    },
    'ETH': {
        'name': 'ETH',
        'icon': '/icon/eth.webp',
        'min_amount': ETH_MIN,
        'max_amount': ETH_MAX,
        'daily_profit': STAKE_ETH_PROFIT,
        'balance_threshold': 10000  # Нужно 10,000₽ на стейковом балансе
    },
    'USDT': {
        'name': 'USDT',
        'icon': '/icon/teher.webp',
        'min_amount': USDT_MIN,
        'max_amount': USDT_MAX,
        'daily_profit': STAKE_USDT_PROFIT,
        'balance_threshold': 100000  # Нужно 100,000₽ на стейковом балансе
    }
}

try:
    # Добавляем корневую директорию в путь для импорта config
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if root_path not in sys.path:
        sys.path.insert(0, root_path)
    
    from config import (
        FAKE_ONLINE_DIAPASON_MIN, FAKE_ONLINE_DIAPASON_MAX, ONLINE_UPDATE_DELAY,
        DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME, BOT_USERNAME,
        REFERRAL_BONUS_PERCENT, DEPOSIT_BONUS_PERCENT
    )
    print(f"✅ Конфигурация загружена: ADMIN_IDS импортирован")
except ImportError as e:
    print(f"⚠️ Ошибка импорта конфига: {e}")
    # Fallback значения если конфиг недоступен
    FAKE_ONLINE_DIAPASON_MIN = 100
    FAKE_ONLINE_DIAPASON_MAX = 1500
    ONLINE_UPDATE_DELAY = 300.0  # 5 минут по умолчанию
    BOT_USERNAME = "Illussion_DMbot"  # Fallback значение для имени бота
    DB_USERNAME = "root"
    DB_PASSWORD = "root"
    DB_HOST = "127.0.0.1"
    DB_PORT = 3306
    DB_NAME = "royal_apl"
    REFERRAL_BONUS_PERCENT = 2.7
    DEPOSIT_BONUS_PERCENT = 10.0

app = FastAPI(title="Royal APL API")

# Добавляем CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешаем все домены
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все методы
    allow_headers=["*"],  # Разрешаем все заголовки
)

# Путь к статическим файлам
STATIC_DIR = os.path.join(os.path.dirname(__file__), "dist")

# Модели данных
class UserCreate(BaseModel):
    username: str
    telegram_id: int
    ref: Optional[str] = None

class UserStats(BaseModel):
    id: int
    username: str
    xp: str
    telegram_id: int
    balance: float
    stake_balance: float
    profit_all: float
    partners_balance: float
    ref: Optional[str]
    create_account: datetime

class StakeRequest(BaseModel):
    telegram_id: int
    amount: float

class StakeStats(BaseModel):
    telegram_id: int
    current_tariff: str
    stake_balance: float
    accumulated_profit: float
    daily_profit_rate: float
    min_amount: float
    max_amount: float
    tariff_icon: str

class MoneyLogEntry(BaseModel):
    id: int
    telegram_id: int
    action: str
    amount: float
    created_at: datetime

class DepositRequest(BaseModel):
    telegram_id: int
    amount: float
    payment_type: str = 'СБП'
    payment_details: Optional[dict] = None

class DepositApproval(BaseModel):
    request_id: int
    approved: bool
    admin_id: int

# Функция подключения к базе данных
def get_db_connection():
    """Создает подключение к MySQL базе данных"""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USERNAME,
            password=DB_PASSWORD,
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"❌ Ошибка подключения к базе данных: {e}")
        return None

# Функции для работы с пользователями
def create_user_in_db(username: str, telegram_id: int, ref: str = None) -> dict:
    """Создает нового пользователя в базе данных"""
    connection = get_db_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Ошибка подключения к базе данных")
    
    try:
        cursor = connection.cursor()
        
        # Проверяем, существует ли уже пользователь с таким telegram_ID
        check_query = "SELECT id FROM users WHERE telegram_ID = %s"
        cursor.execute(check_query, (telegram_id,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            return {"status": "exists", "user_id": existing_user[0]}
        
        # Создаем нового пользователя (только основные поля)
        insert_query = """
            INSERT INTO users (username, XP, telegram_ID, ref, create_accaunt) 
            VALUES (%s, %s, %s, %s, %s)
        """
        
        current_time = datetime.now()
        values = (
            username,
            "0/100",  # Начальный XP
            telegram_id,
            ref,      # Реферальный код
            current_time
        )
        
        cursor.execute(insert_query, values)
        connection.commit()
        
        user_id = cursor.lastrowid
        
        print(f"✅ Пользователь создан: ID={user_id}, Telegram ID={telegram_id}, Username={username}")
        
        return {
            "status": "created",
            "user_id": user_id,
            "telegram_id": telegram_id,
            "username": username,
            "xp": "0/100",
            "created_at": current_time.isoformat()
        }
        
    except Error as e:
        print(f"❌ Ошибка создания пользователя: {e}")
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Ошибка создания пользователя: {str(e)}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_user_stats_by_telegram_id(telegram_id: int) -> dict:
    """Получает статистику пользователя по Telegram ID"""
    connection = get_db_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Ошибка подключения к базе данных")
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        query = """
            SELECT id, username, XP, telegram_ID, balance, stake_balance, 
                   profit_all, partners_balance, ref, create_accaunt
            FROM users WHERE telegram_ID = %s
        """
        
        cursor.execute(query, (telegram_id,))
        user = cursor.fetchone()
        
        if not user:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        
        # Парсим XP для прогресс бара
        xp_current, xp_max = 0, 100
        if user['XP'] and '/' in user['XP']:
            try:
                xp_parts = user['XP'].split('/')
                xp_current = int(xp_parts[0])
                xp_max = int(xp_parts[1])
            except (ValueError, IndexError):
                print(f"⚠️ Неверный формат XP: {user['XP']}")
        
        # Вычисляем уровень (грубо, на основе общего XP)
        total_completed_xp = (xp_current / xp_max) * 100 if xp_max > 0 else 0
        level = max(1, int(total_completed_xp // 100) + 1)
        
        return {
            "id": user['id'],
            "username": user['username'],
            "telegram_id": user['telegram_ID'],
            "balance": user['balance'],
            "stake_balance": user['stake_balance'],
            "profit_all": user['profit_all'],
            "partners_balance": user['partners_balance'],
            "ref": user['ref'],
            "create_account": user['create_accaunt'].isoformat() if user['create_accaunt'] else None,
            "xp": {
                "raw": user['XP'],
                "current": xp_current,
                "max": xp_max,
                "percentage": (xp_current / xp_max * 100) if xp_max > 0 else 0,
                "level": level
            }
        }
        
    except Error as e:
        print(f"❌ Ошибка получения данных пользователя: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка базы данных: {str(e)}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Глобальная переменная для кеширования онлайна
_cached_online_data = {
    'value': None,
    'last_update': 0,
    'trend_direction': random.choice([-1, 1]),
    'trend_strength': random.uniform(0.3, 0.8),
    'trend_counter': 0,
    'trend_duration': random.randint(5, 15),
    'phase': random.random() * math.pi * 2
}

# Глобальные переменные для расчета прибыли стейкинга
_stake_profit_cache = {
    'last_update': 0,
    'user_profits': {}  # {telegram_id: {'last_calculated': timestamp, 'accumulated': amount}}
}

def get_current_online():
    """
    Генерирует текущее значение онлайна на основе времени
    Использует ONLINE_UPDATE_DELAY из конфига для определения частоты обновлений
    Повторяет алгоритм из fake_online.py для консистентности
    """
    current_time = time.time()
    global _cached_online_data
    
    # Проверяем, нужно ли обновить значение согласно ONLINE_UPDATE_DELAY
    if (_cached_online_data['value'] is None or 
        (current_time - _cached_online_data['last_update']) >= ONLINE_UPDATE_DELAY):
        
        print(f"📊 Обновление онлайна (прошло {current_time - _cached_online_data['last_update']:.1f} сек)")
        
        # Инициализируем если первый раз
        if _cached_online_data['value'] is None:
            _cached_online_data['value'] = random.randint(FAKE_ONLINE_DIAPASON_MIN, FAKE_ONLINE_DIAPASON_MAX)
        
        current_online = _cached_online_data['value']
        
        # Смена тренда через определённое время  
        _cached_online_data['trend_counter'] += 1
        if _cached_online_data['trend_counter'] >= _cached_online_data['trend_duration']:
            _cached_online_data['trend_direction'] = random.choice([-1, 1])
            _cached_online_data['trend_strength'] = random.uniform(0.3, 0.8)
            _cached_online_data['trend_duration'] = random.randint(5, 15)
            _cached_online_data['trend_counter'] = 0
            print(f"🔄 Смена тренда: направление={_cached_online_data['trend_direction']}")
        
        # Основной тренд (рост или падение)
        trend_change = (_cached_online_data['trend_direction'] * 
                       _cached_online_data['trend_strength'] * 
                       random.uniform(0.5, 1.5))
        
        # Плавная волна (суточные колебания)
        wave = (math.sin(_cached_online_data['phase']) * 
                (FAKE_ONLINE_DIAPASON_MAX - FAKE_ONLINE_DIAPASON_MIN) * 0.03)
        _cached_online_data['phase'] += random.uniform(0.08, 0.12)
        
        # Малые случайные флуктуации
        noise = random.uniform(-5, 5)
        
        # Случайные резкие изменения (события: приход/уход группы людей)
        spike = 0
        if random.random() < 0.05:  # 5% шанс резкого изменения
            spike = random.choice([-1, 1]) * random.uniform(10, 30)
            print(f"⚡ Резкий скачок: {spike:+.1f}")
        
        # Суммарное изменение
        total_change = trend_change + wave + noise + spike
        current_online += total_change
        
        # Ограничиваем в пределах диапазона с эффектом отскока
        if current_online < FAKE_ONLINE_DIAPASON_MIN:
            current_online = FAKE_ONLINE_DIAPASON_MIN + random.uniform(5, 20)
            _cached_online_data['trend_direction'] = 1  # разворачиваем тренд вверх
            _cached_online_data['trend_counter'] = 0
            print("🔄 Отскок от минимума")
        elif current_online > FAKE_ONLINE_DIAPASON_MAX:
            current_online = FAKE_ONLINE_DIAPASON_MAX - random.uniform(5, 20)
            _cached_online_data['trend_direction'] = -1  # разворачиваем тренд вниз
            _cached_online_data['trend_counter'] = 0
            print("🔄 Отскок от максимума")
        
        # Добавляем естественную неровность
        display_online = int(current_online + random.uniform(-1, 1))
        
        # Обновляем кеш
        _cached_online_data['value'] = display_online
        _cached_online_data['last_update'] = current_time
        
        print(f"📈 Новый онлайн: {display_online} (изменение: {total_change:+.1f})")
    
    return _cached_online_data['value']

# Функции для работы с тарифами
def determine_user_tariff(stake_balance: float) -> str:
    """Определяет тариф пользователя на основе стейкового баланса"""
    if stake_balance >= TARIFF_CONFIG['USDT']['balance_threshold']:
        return 'USDT'
    elif stake_balance >= TARIFF_CONFIG['ETH']['balance_threshold']:
        return 'ETH'
    else:
        return 'TON'

def get_tariff_config(tariff_name: str) -> dict:
    """Получает конфигурацию тарифа"""
    return TARIFF_CONFIG.get(tariff_name, TARIFF_CONFIG['TON'])

# Функции для работы со стейкингом
def update_user_tariff_if_needed(telegram_id: int):
    """Обновляет тариф пользователя если нужно на основе его стейкового баланса"""
    connection = get_db_connection()
    if not connection:
        return False
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Получаем текущий стейковый баланс пользователя
        cursor.execute("SELECT stake_balance, tarifs FROM users WHERE telegram_ID = %s", (str(telegram_id),))
        user = cursor.fetchone()
        
        if not user:
            return False
        
        current_stake_balance = float(user['stake_balance']) if user['stake_balance'] else 0.0
        current_tariff = user['tarifs'] or 'TON'
        
        # Определяем нужный тариф на основе стейкового баланса
        new_tariff = determine_user_tariff(current_stake_balance)
        
        # Если тариф изменился - обновляем
        if new_tariff != current_tariff:
            cursor.execute("UPDATE users SET tarifs = %s WHERE telegram_ID = %s", 
                         (new_tariff, str(telegram_id)))
            connection.commit()
            print(f"✅ Тариф пользователя {telegram_id} обновлен: {current_tariff} → {new_tariff} (стейк баланс: {current_stake_balance})")
            return True
        
        return False
        
    except Error as e:
        print(f"❌ Ошибка обновления тарифа: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def calculate_stake_profit(stake_amount: float, daily_rate: float, time_elapsed_seconds: float) -> float:
    """Рассчитывает прибыль стейкинга"""
    if stake_amount <= 0 or daily_rate <= 0:
        return 0.0
    
    # Конвертируем дневную ставку в секундную
    seconds_per_day = 24 * 60 * 60
    rate_per_second = daily_rate / 100.0 / seconds_per_day
    
    # Рассчитываем прибыль за прошедшее время
    profit = stake_amount * rate_per_second * time_elapsed_seconds
    return round(profit, 6)

def get_user_accumulated_profit(telegram_id: int) -> float:
    """Получает накопленную прибыль пользователя с учетом времени"""
    connection = get_db_connection()
    if not connection:
        return 0.0
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Получаем данные пользователя
        cursor.execute("""
            SELECT stake_balance, tarifs, profit_all, create_accaunt 
            FROM users WHERE telegram_ID = %s
        """, (str(telegram_id),))
        user = cursor.fetchone()
        
        if not user:
            return 0.0
        
        stake_balance = float(user['stake_balance']) if user['stake_balance'] else 0.0
        if stake_balance <= 0:
            return 0.0
        
        current_tariff = user['tarifs'] or 'TON'
        tariff_config = get_tariff_config(current_tariff)
        
        current_time = time.time()
        
        # Проверяем кеш для этого пользователя
        user_id_str = str(telegram_id)
        if user_id_str in _stake_profit_cache['user_profits']:
            cached_data = _stake_profit_cache['user_profits'][user_id_str]
            last_calculated = cached_data.get('last_calculated', current_time)
            accumulated = cached_data.get('accumulated', 0.0)
        else:
            # Первый расчет - начинаем с текущего времени
            last_calculated = current_time
            accumulated = 0.0
            _stake_profit_cache['user_profits'][user_id_str] = {
                'last_calculated': last_calculated,
                'accumulated': accumulated
            }
        
        # Рассчитываем прибыль с последнего обновления
        time_elapsed = current_time - last_calculated
        
        if time_elapsed >= PROFIT_UPDATE_INTERVAL:
            new_profit = calculate_stake_profit(
                stake_balance, 
                tariff_config['daily_profit'], 
                time_elapsed
            )
            
            accumulated += new_profit
            
            # Обновляем кеш
            _stake_profit_cache['user_profits'][user_id_str] = {
                'last_calculated': current_time,
                'accumulated': accumulated
            }
        
        return round(accumulated, 6)
        
    except Error as e:
        print(f"❌ Ошибка расчета прибыли: {e}")
        return 0.0
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def create_stake_investment(telegram_id: int, amount: float) -> dict:
    """Создает инвестицию в стейкинг"""
    connection = get_db_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Ошибка подключения к базе данных")
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Получаем данные пользователя
        cursor.execute("""
            SELECT balance, stake_balance, tarifs 
            FROM users WHERE telegram_ID = %s
        """, (str(telegram_id),))
        user = cursor.fetchone()
        
        if not user:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        
        current_balance = float(user['balance']) if user['balance'] else 0.0
        current_stake = float(user['stake_balance']) if user['stake_balance'] else 0.0
        current_tariff = user['tarifs'] or 'TON'
        
        # Проверяем достаточность средств
        if current_balance < amount:
            raise HTTPException(status_code=400, detail="Недостаточно средств на балансе")
        
        # Получаем конфигурацию тарифа
        tariff_config = get_tariff_config(current_tariff)
        
        # Проверяем минимальную и максимальную сумму
        if amount < tariff_config['min_amount']:
            raise HTTPException(status_code=400, 
                              detail=f"Минимальная сумма для инвестирования: {tariff_config['min_amount']}")
        
        if amount > tariff_config['max_amount']:
            raise HTTPException(status_code=400, 
                              detail=f"Максимальная сумма для инвестирования: {tariff_config['max_amount']}")
        
        # Обновляем балансы
        new_balance = current_balance - amount
        new_stake_balance = current_stake + amount
        
        cursor.execute("""
            UPDATE users 
            SET balance = %s, stake_balance = %s 
            WHERE telegram_ID = %s
        """, (str(new_balance), str(new_stake_balance), str(telegram_id)))
        
        connection.commit()
        
        # Инициализируем кеш прибыли для пользователя
        current_time = time.time()
        _stake_profit_cache['user_profits'][str(telegram_id)] = {
            'last_calculated': current_time,
            'accumulated': 0.0
        }
        
        # Логируем операции (списание с основного баланса и пополнение стейка)
        add_money_log(telegram_id, 'withdraw', -amount)  # Списание с основного баланса
        add_money_log(telegram_id, 'dep_stake', amount)  # Пополнение стейк баланса
        
        print(f"✅ Инвестиция создана: пользователь {telegram_id}, сумма {amount}")
        
        return {
            "success": True,
            "message": "Инвестиция успешно создана",
            "data": {
                "invested_amount": amount,
                "new_balance": new_balance,
                "new_stake_balance": new_stake_balance,
                "tariff": current_tariff
            }
        }
        
    except Error as e:
        print(f"❌ Ошибка создания инвестиции: {e}")
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Ошибка создания инвестиции: {str(e)}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def collect_stake_profit(telegram_id: int) -> dict:
    """Собирает накопленную прибыль со стейкинга"""
    connection = get_db_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Ошибка подключения к базе данных")
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Получаем накопленную прибыль
        accumulated_profit = get_user_accumulated_profit(telegram_id)
        
        if accumulated_profit <= 0:
            return {
                "success": False,
                "message": "Нет прибыли для сбора",
                "data": {"collected_amount": 0}
            }
        
        # Получаем текущий баланс пользователя
        cursor.execute("""
            SELECT balance, profit_all 
            FROM users WHERE telegram_ID = %s
        """, (str(telegram_id),))
        user = cursor.fetchone()
        
        if not user:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        
        current_balance = float(user['balance']) if user['balance'] else 0.0
        current_profit_all = float(user['profit_all']) if user['profit_all'] else 0.0
        
        # Обновляем балансы
        new_balance = current_balance + accumulated_profit
        new_profit_all = current_profit_all + accumulated_profit
        
        cursor.execute("""
            UPDATE users 
            SET balance = %s, profit_all = %s 
            WHERE telegram_ID = %s
        """, (str(new_balance), str(new_profit_all), str(telegram_id)))
        
        connection.commit()
        
        # Сбрасываем кеш прибыли для пользователя
        current_time = time.time()
        _stake_profit_cache['user_profits'][str(telegram_id)] = {
            'last_calculated': current_time,
            'accumulated': 0.0
        }
        
        # Логируем операцию
        add_money_log(telegram_id, 'stake_profit', accumulated_profit)
        
        print(f"✅ Прибыль собрана: пользователь {telegram_id}, сумма {accumulated_profit}")
        
        return {
            "success": True,
            "message": "Прибыль успешно собрана",
            "data": {
                "collected_amount": accumulated_profit,
                "new_balance": new_balance,
                "total_profit": new_profit_all
            }
        }
        
    except Error as e:
        print(f"❌ Ошибка сбора прибыли: {e}")
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Ошибка сбора прибыли: {str(e)}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def withdraw_from_stake(telegram_id: int, amount: float) -> dict:
    """Выводит средства со стейкового баланса на основной баланс"""
    connection = get_db_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Ошибка подключения к базе данных")
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Получаем данные пользователя
        cursor.execute("""
            SELECT balance, stake_balance 
            FROM users WHERE telegram_ID = %s
        """, (str(telegram_id),))
        user = cursor.fetchone()
        
        if not user:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        
        current_balance = float(user['balance']) if user['balance'] else 0.0
        current_stake_balance = float(user['stake_balance']) if user['stake_balance'] else 0.0
        
        # Проверяем достаточность средств на стейк балансе
        if current_stake_balance < amount:
            raise HTTPException(status_code=400, detail="Недостаточно средств на стейк балансе")
        
        if amount <= 0:
            raise HTTPException(status_code=400, detail="Сумма должна быть больше нуля")
        
        # Обновляем балансы
        new_balance = current_balance + amount
        new_stake_balance = current_stake_balance - amount
        
        cursor.execute("""
            UPDATE users 
            SET balance = %s, stake_balance = %s 
            WHERE telegram_ID = %s
        """, (str(new_balance), str(new_stake_balance), str(telegram_id)))
        
        connection.commit()
        
        # Логируем операции (вывод со стейка и пополнение основного баланса)
        add_money_log(telegram_id, 'withdraw_stake', -amount)  # Списание со стейк баланса
        add_money_log(telegram_id, 'dep', amount)  # Пополнение основного баланса
        
        print(f"✅ Вывод со стейка: пользователь {telegram_id}, сумма {amount}")
        
        return {
            "success": True,
            "message": "Средства успешно выведены со стейка",
            "data": {
                "withdrawn_amount": amount,
                "new_balance": new_balance,
                "new_stake_balance": new_stake_balance
            }
        }
        
    except Error as e:
        print(f"❌ Ошибка вывода со стейка: {e}")
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Ошибка вывода средств: {str(e)}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def add_balance(telegram_id: int, amount: float, action: str = 'dep') -> dict:
    """Добавляет средства на основной баланс пользователя"""
    connection = get_db_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Ошибка подключения к базе данных")
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Получаем данные пользователя
        cursor.execute("""
            SELECT balance FROM users WHERE telegram_ID = %s
        """, (str(telegram_id),))
        user = cursor.fetchone()
        
        if not user:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        
        current_balance = float(user['balance']) if user['balance'] else 0.0
        
        if amount <= 0:
            raise HTTPException(status_code=400, detail="Сумма должна быть больше нуля")
        
        # Обновляем баланс
        new_balance = current_balance + amount
        
        cursor.execute("""
            UPDATE users 
            SET balance = %s 
            WHERE telegram_ID = %s
        """, (str(new_balance), str(telegram_id)))
        
        connection.commit()
        
        # Логируем операцию
        add_money_log(telegram_id, action, amount)
        
        print(f"✅ Баланс пополнен: пользователь {telegram_id}, сумма {amount}, действие {action}")
        
        return {
            "success": True,
            "message": "Баланс успешно пополнен",
            "data": {
                "added_amount": amount,
                "new_balance": new_balance,
                "action": action
            }
        }
        
    except Error as e:
        print(f"❌ Ошибка пополнения баланса: {e}")
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Ошибка пополнения баланса: {str(e)}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def withdraw_balance(telegram_id: int, amount: float, action: str = 'withdraw') -> dict:
    """Списывает средства с основного баланса пользователя"""
    connection = get_db_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Ошибка подключения к базе данных")
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Получаем данные пользователя
        cursor.execute("""
            SELECT balance FROM users WHERE telegram_ID = %s
        """, (str(telegram_id),))
        user = cursor.fetchone()
        
        if not user:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        
        current_balance = float(user['balance']) if user['balance'] else 0.0
        
        if amount <= 0:
            raise HTTPException(status_code=400, detail="Сумма должна быть больше нуля")
            
        if current_balance < amount:
            raise HTTPException(status_code=400, detail="Недостаточно средств на балансе")
        
        # Обновляем баланс
        new_balance = current_balance - amount
        
        cursor.execute("""
            UPDATE users 
            SET balance = %s 
            WHERE telegram_ID = %s
        """, (str(new_balance), str(telegram_id)))
        
        connection.commit()
        
        # Логируем операцию
        add_money_log(telegram_id, action, -amount)
        
        print(f"✅ Средства списаны: пользователь {telegram_id}, сумма {amount}, действие {action}")
        
        return {
            "success": True,
            "message": "Средства успешно списаны",
            "data": {
                "withdrawn_amount": amount,
                "new_balance": new_balance,
                "action": action
            }
        }
        
    except Error as e:
        print(f"❌ Ошибка списания средств: {e}")
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Ошибка списания средств: {str(e)}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_stake_stats(telegram_id: int) -> dict:
    """Получает статистику стейкинга пользователя"""
    connection = get_db_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Ошибка подключения к базе данных")
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Сначала обновляем тариф если нужно
        update_user_tariff_if_needed(telegram_id)
        
        # Получаем данные пользователя
        cursor.execute("""
            SELECT balance, stake_balance, tarifs, profit_all 
            FROM users WHERE telegram_ID = %s
        """, (str(telegram_id),))
        user = cursor.fetchone()
        
        if not user:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        
        current_tariff = user['tarifs'] or 'TON'
        tariff_config = get_tariff_config(current_tariff)
        
        stake_balance = float(user['stake_balance']) if user['stake_balance'] else 0.0
        accumulated_profit = get_user_accumulated_profit(telegram_id)
        
        return {
            "success": True,
            "data": {
                "telegram_id": telegram_id,
                "current_tariff": current_tariff,
                "tariff_name": tariff_config['name'],
                "tariff_icon": tariff_config['icon'],
                "stake_balance": stake_balance,
                "accumulated_profit": accumulated_profit,
                "daily_profit_rate": tariff_config['daily_profit'],
                "min_amount": tariff_config['min_amount'],
                "max_amount": tariff_config['max_amount'],
                "balance": float(user['balance']) if user['balance'] else 0.0,
                "total_profit": float(user['profit_all']) if user['profit_all'] else 0.0
            }
        }
        
    except Error as e:
        print(f"❌ Ошибка получения статистики стейкинга: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка получения статистики: {str(e)}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Подключение всех статических файлов
if os.path.exists(STATIC_DIR):
    # Подключаем все статические директории
    app.mount("/assets", StaticFiles(directory=os.path.join(STATIC_DIR, "assets")), name="assets")
    app.mount("/font", StaticFiles(directory=os.path.join(STATIC_DIR, "font")), name="font")
    app.mount("/icon", StaticFiles(directory=os.path.join(STATIC_DIR, "icon")), name="icon")
    app.mount("/img", StaticFiles(directory=os.path.join(STATIC_DIR, "img")), name="img")
    app.mount("/img-scroll", StaticFiles(directory=os.path.join(STATIC_DIR, "img-scroll")), name="img_scroll")
    app.mount("/sound", StaticFiles(directory=os.path.join(STATIC_DIR, "sound")), name="sound")

@app.get("/")
def read_root():
    """Главная страница - отдаем index.html"""
    index_path = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path, media_type="text/html")
    return {"message": "API Server Running", "status": "OK"}

@app.get("/favicon.ico")
def favicon():
    """Favicon"""
    favicon_path = os.path.join(STATIC_DIR, "favicon.ico")
    if os.path.exists(favicon_path):
        return FileResponse(favicon_path)
    return {"message": "Favicon not found"}

@app.get("/api/status")
def get_status():
    """API статус"""
    return {"status": "running", "service": "Royal APL API"}

@app.get("/api/online")
def get_online():
    """Получить текущий онлайн"""
    current_time = time.time()
    current_online = get_current_online()
    
    # Вычисляем время следующего обновления
    time_since_last_update = current_time - _cached_online_data['last_update']
    time_to_next_update = ONLINE_UPDATE_DELAY - time_since_last_update
    next_update_timestamp = int(current_time + time_to_next_update)
    
    return {
        "online": current_online,
        "timestamp": int(current_time),
        "last_update": int(_cached_online_data['last_update']),
        "next_update": next_update_timestamp,
        "time_to_next_update": int(time_to_next_update),
        "update_interval": int(ONLINE_UPDATE_DELAY),
        "min_range": FAKE_ONLINE_DIAPASON_MIN,
        "max_range": FAKE_ONLINE_DIAPASON_MAX
    }

# Функции для работы с реферальной системой
def get_referral_stats_by_telegram_id(telegram_id: int) -> dict:
    """Получает статистику рефералов пользователя"""
    connection = get_db_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Ошибка подключения к базе данных")
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Получаем количество рефералов
        referrals_query = """
            SELECT COUNT(*) as partners_count, 
                   COALESCE(SUM(CASE WHEN partners_balance IS NOT NULL AND partners_balance != '' 
                                   THEN CAST(partners_balance AS DECIMAL(10,2)) 
                                   ELSE 0 END), 0) as total_earnings
            FROM users 
            WHERE ref = %s
        """
        
        cursor.execute(referrals_query, (str(telegram_id),))
        result = cursor.fetchone()
        
        return {
            "partners_count": result["partners_count"] if result else 0,
            "total_earnings": float(result["total_earnings"]) if result and result["total_earnings"] else 0.0
        }
        
    except Error as e:
        print(f"❌ Ошибка получения реферальной статистики: {e}")
        return {"partners_count": 0, "total_earnings": 0.0}
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_detailed_referral_stats_by_telegram_id(telegram_id: int) -> dict:
    """Получает детальную статистику рефералов пользователя по уровням"""
    connection = get_db_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Ошибка подключения к базе данных")
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Партнеры 1 уровня (прямые рефералы)
        level1_query = """
            SELECT COUNT(*) as level1_count,
                   COUNT(CASE WHEN stake_balance IS NOT NULL AND CAST(stake_balance AS DECIMAL(10,2)) > 0 
                             THEN 1 END) as level1_active
            FROM users 
            WHERE ref = %s
        """
        
        cursor.execute(level1_query, (str(telegram_id),))
        level1_result = cursor.fetchone()
        
        # Получаем telegram_ID всех рефералов 1 уровня для поиска их рефералов
        level1_ids_query = """
            SELECT telegram_ID 
            FROM users 
            WHERE ref = %s
        """
        
        cursor.execute(level1_ids_query, (str(telegram_id),))
        level1_ids = cursor.fetchall()
        
        level2_count = 0
        level3_count = 0
        level23_active = 0
        
        if level1_ids:
            # Формируем список ID для поиска партнеров 2 уровня
            level1_telegram_ids = [str(row['telegram_ID']) for row in level1_ids]
            
            if level1_telegram_ids:
                # Партнеры 2 уровня (рефералы рефералов)
                level2_query = f"""
                    SELECT COUNT(*) as level2_count,
                           COUNT(CASE WHEN stake_balance IS NOT NULL AND CAST(stake_balance AS DECIMAL(10,2)) > 0 
                                     THEN 1 END) as level2_active,
                           GROUP_CONCAT(telegram_ID) as level2_ids
                    FROM users 
                    WHERE ref IN ({','.join(['%s'] * len(level1_telegram_ids))})
                """
                
                cursor.execute(level2_query, level1_telegram_ids)
                level2_result = cursor.fetchone()
                
                level2_count = level2_result['level2_count'] if level2_result else 0
                level23_active += level2_result['level2_active'] if level2_result and level2_result['level2_active'] else 0
                
                # Получаем ID партнеров 2 уровня для поиска партнеров 3 уровня
                if level2_result and level2_result['level2_ids']:
                    level2_telegram_ids = level2_result['level2_ids'].split(',')
                    
                    # Партнеры 3 уровня
                    level3_query = f"""
                        SELECT COUNT(*) as level3_count,
                               COUNT(CASE WHEN stake_balance IS NOT NULL AND CAST(stake_balance AS DECIMAL(10,2)) > 0 
                                         THEN 1 END) as level3_active
                        FROM users 
                        WHERE ref IN ({','.join(['%s'] * len(level2_telegram_ids))})
                    """
                    
                    cursor.execute(level3_query, level2_telegram_ids)
                    level3_result = cursor.fetchone()
                    
                    level3_count = level3_result['level3_count'] if level3_result else 0
                    level23_active += level3_result['level3_active'] if level3_result and level3_result['level3_active'] else 0
        
        # Общие активные партнеры
        total_active = (level1_result['level1_active'] if level1_result and level1_result['level1_active'] else 0) + level23_active
        
        return {
            "level1_partners": level1_result['level1_count'] if level1_result else 0,
            "level1_active": level1_result['level1_active'] if level1_result and level1_result['level1_active'] else 0,
            "level2_partners": level2_count,
            "level3_partners": level3_count,
            "level23_partners": level2_count + level3_count,
            "level23_active": level23_active,
            "total_partners": (level1_result['level1_count'] if level1_result else 0) + level2_count + level3_count,
            "active_partners": total_active
        }
        
    except Error as e:
        print(f"❌ Ошибка получения детальной реферальной статистики: {e}")
        return {
            "level1_partners": 0,
            "level1_active": 0,
            "level2_partners": 0,
            "level3_partners": 0,
            "level23_partners": 0,
            "level23_active": 0,
            "total_partners": 0,
            "active_partners": 0
        }
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def generate_referral_link_api(telegram_id: int) -> str:
    """Генерирует реферальную ссылку для API"""
    return f"https://t.me/{BOT_USERNAME}?start=ref_{telegram_id}"

# Функции для работы с денежными логами
def add_money_log(telegram_id: int, action: str, amount: float) -> bool:
    """Добавляет запись в лог денежных операций"""
    connection = get_db_connection()
    if not connection:
        print(f"❌ Не удалось подключиться к БД для логирования: {action} {amount} для {telegram_id}")
        return False
    
    try:
        cursor = connection.cursor()
        
        # Добавляем запись в лог
        insert_query = """
            INSERT INTO money_log (telegram_id, action, amount, created_at) 
            VALUES (%s, %s, %s, %s)
        """
        
        current_time = datetime.now()
        values = (str(telegram_id), action, str(amount), current_time)
        
        cursor.execute(insert_query, values)
        connection.commit()
        
        print(f"💰 Лог добавлен: {telegram_id} | {action} | {amount:+.2f}₽")
        return True
        
    except Error as e:
        print(f"❌ Ошибка добавления лога: {e}")
        connection.rollback()
        return False
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_money_logs_by_telegram_id(telegram_id: int, limit: int = 50, offset: int = 0) -> list:
    """Получает историю денежных операций пользователя"""
    connection = get_db_connection()
    if not connection:
        return []
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Получаем историю операций
        query = """
            SELECT id, telegram_id, action, amount, created_at
            FROM money_log 
            WHERE telegram_id = %s
            ORDER BY created_at DESC
            LIMIT %s OFFSET %s
        """
        
        cursor.execute(query, (str(telegram_id), limit, offset))
        logs = cursor.fetchall()
        
        # Форматируем результат
        formatted_logs = []
        for log in logs:
            # Определяем описание действия
            action_descriptions = {
                'withdraw': 'Вывод средств с баланса',
                'withdraw_stake': 'Вывод со стейка на баланс',
                'dep': 'Пополнение баланса',
                'dep_stake': 'Инвестиция в стейк',
                'dep_ref': 'Реферальный бонус',
                'stake_profit': 'Прибыль со стейка'
            }
            
            formatted_logs.append({
                "id": log["id"],
                "telegram_id": log["telegram_id"],
                "action": log["action"],
                "action_description": action_descriptions.get(log["action"], log["action"]),
                "amount": float(log["amount"]) if log["amount"] else 0.0,
                "created_at": log["created_at"].isoformat() if log["created_at"] else None,
                "is_positive": float(log["amount"]) > 0 if log["amount"] else False
            })
        
        return formatted_logs
        
    except Error as e:
        print(f"❌ Ошибка получения истории операций: {e}")
        return []
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_money_logs_count_by_telegram_id(telegram_id: int) -> int:
    """Получает общее количество денежных операций пользователя"""
    connection = get_db_connection()
    if not connection:
        return 0
    
    try:
        cursor = connection.cursor()
        
        query = "SELECT COUNT(*) FROM money_log WHERE telegram_id = %s"
        cursor.execute(query, (str(telegram_id),))
        
        result = cursor.fetchone()
        return result[0] if result else 0
        
    except Error as e:
        print(f"❌ Ошибка получения количества операций: {e}")
        return 0
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Функции для работы с запросами на пополнение
def add_notification_to_queue(notification_type: str, data: dict) -> bool:
    """Добавляет уведомление в очередь для отправки ботом"""
    connection = get_db_connection()
    if not connection:
        return False
    
    try:
        cursor = connection.cursor()
        
        insert_query = """
            INSERT INTO notifications_queue (type, data, created_at)
            VALUES (%s, %s, %s)
        """
        
        current_time = datetime.now()
        data_json = json.dumps(data)
        
        cursor.execute(insert_query, (notification_type, data_json, current_time))
        connection.commit()
        
        print(f"✅ Уведомление добавлено в очередь: Type={notification_type}")
        return True
        
    except Error as e:
        print(f"❌ Ошибка добавления уведомления в очередь: {e}")
        connection.rollback()
        return False
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def create_deposit_request_in_db(telegram_id: int, amount: float, payment_type: str, payment_details: dict = None) -> dict:
    """Создает запрос на пополнение баланса"""
    connection = get_db_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Ошибка подключения к базе данных")
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Получаем данные пользователя
        cursor.execute("SELECT username FROM users WHERE telegram_ID = %s", (str(telegram_id),))
        user = cursor.fetchone()
        
        if not user:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        
        # Рассчитываем бонус
        bonus_amount = round(amount * (DEPOSIT_BONUS_PERCENT / 100), 2)
        total_amount = amount + bonus_amount
        
        # Создаем запрос на пополнение
        insert_query = """
            INSERT INTO deposit_requests 
            (telegram_id, username, amount, bonus_amount, total_amount, payment_type, payment_details, status, created_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        current_time = datetime.now()
        payment_details_json = json.dumps(payment_details) if payment_details else None
        
        values = (
            str(telegram_id),
            user['username'],
            str(amount),
            str(bonus_amount),
            str(total_amount),
            payment_type,
            payment_details_json,
            'pending',  # Статус: pending, approved, rejected
            current_time
        )
        
        cursor.execute(insert_query, values)
        connection.commit()
        
        request_id = cursor.lastrowid
        
        result_data = {
            "request_id": request_id,
            "telegram_id": telegram_id,
            "username": user['username'],
            "amount": amount,
            "bonus_amount": bonus_amount,
            "total_amount": total_amount,
            "payment_type": payment_type,
            "status": "pending",
            "created_at": current_time.isoformat()
        }
        
        # Добавляем уведомление в очередь для админов
        add_notification_to_queue('deposit_request', result_data)
        
        print(f"✅ Запрос на пополнение создан: ID={request_id}, User={telegram_id}, Amount={amount}, Bonus={bonus_amount}")
        
        return result_data
        
    except Error as e:
        print(f"❌ Ошибка создания запроса на пополнение: {e}")
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Ошибка создания запроса: {str(e)}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_deposit_request_by_id(request_id: int) -> dict:
    """Получает запрос на пополнение по ID"""
    connection = get_db_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Ошибка подключения к базе данных")
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        query = """
            SELECT id, telegram_id, username, amount, bonus_amount, total_amount,
                   payment_type, payment_details, status, created_at, processed_at, processed_by
            FROM deposit_requests
            WHERE id = %s
        """
        
        cursor.execute(query, (request_id,))
        request = cursor.fetchone()
        
        if not request:
            raise HTTPException(status_code=404, detail="Запрос не найден")
        
        return {
            "id": request['id'],
            "telegram_id": request['telegram_id'],
            "username": request['username'],
            "amount": float(request['amount']) if request['amount'] else 0.0,
            "bonus_amount": float(request['bonus_amount']) if request['bonus_amount'] else 0.0,
            "total_amount": float(request['total_amount']) if request['total_amount'] else 0.0,
            "payment_type": request['payment_type'],
            "payment_details": json.loads(request['payment_details']) if request['payment_details'] else None,
            "status": request['status'],
            "created_at": request['created_at'].isoformat() if request['created_at'] else None,
            "processed_at": request['processed_at'].isoformat() if request['processed_at'] else None,
            "processed_by": request['processed_by']
        }
        
    except Error as e:
        print(f"❌ Ошибка получения запроса на пополнение: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка получения запроса: {str(e)}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_last_deposit_request_by_telegram_id(telegram_id: int) -> dict:
    """Получает последний запрос на пополнение пользователя"""
    connection = get_db_connection()
    if not connection:
        return None
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        query = """
            SELECT id, telegram_id, username, amount, bonus_amount, total_amount,
                   payment_type, status, created_at
            FROM deposit_requests
            WHERE telegram_id = %s
            ORDER BY created_at DESC
            LIMIT 1
        """
        
        cursor.execute(query, (str(telegram_id),))
        request = cursor.fetchone()
        
        if not request:
            return None
        
        return {
            "id": request['id'],
            "telegram_id": request['telegram_id'],
            "username": request['username'],
            "amount": float(request['amount']) if request['amount'] else 0.0,
            "bonus_amount": float(request['bonus_amount']) if request['bonus_amount'] else 0.0,
            "total_amount": float(request['total_amount']) if request['total_amount'] else 0.0,
            "payment_type": request['payment_type'],
            "status": request['status'],
            "created_at": request['created_at'].isoformat() if request['created_at'] else None
        }
        
    except Error as e:
        print(f"❌ Ошибка получения последнего запроса: {e}")
        return None
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def approve_deposit_request(request_id: int, admin_id: int) -> dict:
    """Подтверждает запрос на пополнение и зачисляет средства"""
    connection = get_db_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Ошибка подключения к базе данных")
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Получаем данные запроса
        cursor.execute("""
            SELECT telegram_id, amount, bonus_amount, total_amount, status
            FROM deposit_requests
            WHERE id = %s
        """, (request_id,))
        
        request = cursor.fetchone()
        
        if not request:
            raise HTTPException(status_code=404, detail="Запрос не найден")
        
        if request['status'] != 'pending':
            raise HTTPException(status_code=400, detail=f"Запрос уже обработан со статусом: {request['status']}")
        
        telegram_id = request['telegram_id']
        amount = float(request['amount'])
        total_amount = float(request['total_amount'])
        
        # Получаем текущий баланс пользователя и его реферера
        cursor.execute("SELECT balance, ref FROM users WHERE telegram_ID = %s", (str(telegram_id),))
        user = cursor.fetchone()
        
        if not user:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        
        current_balance = float(user['balance']) if user['balance'] else 0.0
        referrer_id = user['ref']
        
        # Зачисляем средства с бонусом пользователю
        new_balance = current_balance + total_amount
        
        cursor.execute("""
            UPDATE users 
            SET balance = %s 
            WHERE telegram_ID = %s
        """, (str(new_balance), str(telegram_id)))
        
        # Логируем пополнение
        add_money_log(int(telegram_id), 'dep', total_amount)
        
        # Если есть реферер - начисляем ему бонус
        referrer_bonus = 0.0
        if referrer_id:
            referrer_bonus = round(amount * (REFERRAL_BONUS_PERCENT / 100), 2)
            
            # Получаем баланс реферера
            cursor.execute("SELECT balance, partners_balance FROM users WHERE telegram_ID = %s", (str(referrer_id),))
            referrer = cursor.fetchone()
            
            if referrer:
                referrer_balance = float(referrer['balance']) if referrer['balance'] else 0.0
                referrer_partners_balance = float(referrer['partners_balance']) if referrer['partners_balance'] else 0.0
                
                new_referrer_balance = referrer_balance + referrer_bonus
                new_partners_balance = referrer_partners_balance + referrer_bonus
                
                cursor.execute("""
                    UPDATE users 
                    SET balance = %s, partners_balance = %s
                    WHERE telegram_ID = %s
                """, (str(new_referrer_balance), str(new_partners_balance), str(referrer_id)))
                
                # Логируем реферальный бонус
                add_money_log(int(referrer_id), 'dep_ref', referrer_bonus)
                
                print(f"💰 Реферальный бонус начислен: Referrer={referrer_id}, Amount={referrer_bonus}")
        
        # Обновляем статус запроса
        current_time = datetime.now()
        cursor.execute("""
            UPDATE deposit_requests
            SET status = 'approved', processed_at = %s, processed_by = %s
            WHERE id = %s
        """, (current_time, str(admin_id), request_id))
        
        connection.commit()
        
        print(f"✅ Пополнение подтверждено: Request={request_id}, User={telegram_id}, Amount={total_amount}")
        
        return {
            "success": True,
            "message": "Пополнение успешно подтверждено",
            "data": {
                "request_id": request_id,
                "telegram_id": telegram_id,
                "new_balance": new_balance,
                "credited_amount": total_amount,
                "referrer_bonus": referrer_bonus
            }
        }
        
    except Error as e:
        print(f"❌ Ошибка подтверждения пополнения: {e}")
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Ошибка подтверждения: {str(e)}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def reject_deposit_request(request_id: int, admin_id: int) -> dict:
    """Отклоняет запрос на пополнение"""
    connection = get_db_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Ошибка подключения к базе данных")
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Проверяем существование и статус запроса
        cursor.execute("""
            SELECT telegram_id, amount, status
            FROM deposit_requests
            WHERE id = %s
        """, (request_id,))
        
        request = cursor.fetchone()
        
        if not request:
            raise HTTPException(status_code=404, detail="Запрос не найден")
        
        if request['status'] != 'pending':
            raise HTTPException(status_code=400, detail=f"Запрос уже обработан со статусом: {request['status']}")
        
        # Обновляем статус запроса
        current_time = datetime.now()
        cursor.execute("""
            UPDATE deposit_requests
            SET status = 'rejected', processed_at = %s, processed_by = %s
            WHERE id = %s
        """, (current_time, str(admin_id), request_id))
        
        connection.commit()
        
        print(f"❌ Пополнение отклонено: Request={request_id}, User={request['telegram_id']}")
        
        return {
            "success": True,
            "message": "Пополнение отклонено",
            "data": {
                "request_id": request_id,
                "telegram_id": request['telegram_id']
            }
        }
        
    except Error as e:
        print(f"❌ Ошибка отклонения пополнения: {e}")
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Ошибка отклонения: {str(e)}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# API роуты для работы с пользователями
@app.post("/api/user/create")
def create_user_endpoint(user_data: UserCreate):
    """Создание нового пользователя"""
    try:
        result = create_user_in_db(
            username=user_data.username,
            telegram_id=user_data.telegram_id,
            ref=user_data.ref
        )
        
        return {
            "success": True,
            "data": result,
            "message": "Пользователь успешно создан" if result["status"] == "created" else "Пользователь уже существует"
        }
        
    except Exception as e:
        print(f"❌ Ошибка в создании пользователя через API: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/stats/my")
def get_my_stats(telegram_id: int):
    """Получение статистики пользователя по Telegram ID"""
    try:
        user_stats = get_user_stats_by_telegram_id(telegram_id)
        
        return {
            "success": True,
            "data": user_stats,
            "message": "Статистика получена успешно"
        }
        
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"❌ Ошибка получения статистики: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка получения статистики: {str(e)}")

@app.get("/api/user/{telegram_id}")
def get_user_by_telegram_id(telegram_id: int):
    """Получение информации о пользователе по Telegram ID"""
    try:
        user_stats = get_user_stats_by_telegram_id(telegram_id)
        return {
            "success": True,
            "data": user_stats
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API роуты для реферальной системы
@app.get("/api/referral/stats")
def get_referral_stats(telegram_id: int):
    """Получение статистики рефералов пользователя"""
    try:
        referral_stats = get_referral_stats_by_telegram_id(telegram_id)
        
        return {
            "success": True,
            "data": {
                "partners_count": referral_stats["partners_count"],
                "total_earnings": referral_stats["total_earnings"],
                "telegram_id": telegram_id
            },
            "message": "Статистика рефералов получена успешно"
        }
        
    except Exception as e:
        print(f"❌ Ошибка получения реферальной статистики: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка получения реферальной статистики: {str(e)}")

@app.get("/api/referral/detailed-stats")
def get_detailed_referral_stats(telegram_id: int):
    """Получение детальной статистики рефералов пользователя по уровням"""
    try:
        detailed_stats = get_detailed_referral_stats_by_telegram_id(telegram_id)
        
        return {
            "success": True,
            "data": {
                "telegram_id": telegram_id,
                "active_partners": detailed_stats["active_partners"],
                "level1_partners": detailed_stats["level1_partners"],
                "level23_partners": detailed_stats["level23_partners"],
                "level2_partners": detailed_stats["level2_partners"],
                "level3_partners": detailed_stats["level3_partners"],
                "level1_active": detailed_stats["level1_active"],
                "level23_active": detailed_stats["level23_active"],
                "total_partners": detailed_stats["total_partners"]
            },
            "message": "Детальная статистика рефералов получена успешно"
        }
        
    except Exception as e:
        print(f"❌ Ошибка получения детальной реферальной статистики: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка получения детальной реферальной статистики: {str(e)}")

@app.get("/api/referral/link")
def get_referral_link(telegram_id: int):
    """Генерация реферальной ссылки для пользователя"""
    try:
        referral_link = generate_referral_link_api(telegram_id)
        
        return {
            "success": True,
            "data": {
                "referral_link": referral_link,
                "telegram_id": telegram_id,
                "bot_username": BOT_USERNAME
            },
            "message": "Реферальная ссылка сгенерирована успешно"
        }
        
    except Exception as e:
        print(f"❌ Ошибка генерации реферальной ссылки: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка генерации реферальной ссылки: {str(e)}")

@app.get("/api/referral/list")
def get_referral_list(telegram_id: int, limit: int = 50, offset: int = 0):
    """Получение списка рефералов пользователя"""
    connection = get_db_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Ошибка подключения к базе данных")
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Получаем список рефералов
        query = """
            SELECT id, username, XP, telegram_ID, balance, partners_balance, create_accaunt
            FROM users 
            WHERE ref = %s
            ORDER BY create_accaunt DESC
            LIMIT %s OFFSET %s
        """
        
        cursor.execute(query, (str(telegram_id), limit, offset))
        referrals = cursor.fetchall()
        
        # Форматируем результат
        formatted_referrals = []
        for ref in referrals:
            formatted_referrals.append({
                "id": ref["id"],
                "username": ref["username"],
                "telegram_id": ref["telegram_ID"],
                "xp": ref["XP"],
                "balance": ref["balance"],
                "partners_balance": ref["partners_balance"],
                "joined_date": ref["create_accaunt"].isoformat() if ref["create_accaunt"] else None
            })
        
        return {
            "success": True,
            "data": {
                "referrals": formatted_referrals,
                "total_count": len(formatted_referrals),
                "limit": limit,
                "offset": offset
            },
            "message": "Список рефералов получен успешно"
        }
        
    except Error as e:
        print(f"❌ Ошибка получения списка рефералов: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка получения списка рефералов: {str(e)}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# API роуты для стейкинга
@app.post("/api/stake/invest")
def stake_invest(stake_request: StakeRequest):
    """Инвестирование в стейкинг"""
    try:
        result = create_stake_investment(stake_request.telegram_id, stake_request.amount)
        return result
        
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"❌ Ошибка инвестирования в стейкинг: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка инвестирования: {str(e)}")

@app.post("/api/stake/collect")
def stake_collect_profit(telegram_id: int):
    """Сбор прибыли со стейкинга"""
    try:
        result = collect_stake_profit(telegram_id)
        return result
        
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"❌ Ошибка сбора прибыли: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка сбора прибыли: {str(e)}")

@app.post("/api/stake/withdraw")
def stake_withdraw(stake_request: StakeRequest):
    """Вывод средств со стейкового баланса на основной баланс"""
    try:
        result = withdraw_from_stake(stake_request.telegram_id, stake_request.amount)
        return result
        
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"❌ Ошибка вывода со стейка: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка вывода со стейка: {str(e)}")

@app.get("/api/stake/stats")
def get_stake_statistics(telegram_id: int):
    """Получение статистики стейкинга пользователя"""
    try:
        result = get_stake_stats(telegram_id)
        return result
        
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"❌ Ошибка получения статистики стейкинга: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка получения статистики: {str(e)}")

@app.get("/api/stake/tariffs")
def get_available_tariffs():
    """Получение списка всех доступных тарифов"""
    try:
        tariffs = []
        for tariff_key, config in TARIFF_CONFIG.items():
            tariffs.append({
                "code": tariff_key,
                "name": config["name"],
                "icon": config["icon"],
                "min_amount": config["min_amount"],
                "max_amount": config["max_amount"],
                "daily_profit": config["daily_profit"],
                "balance_threshold": config["balance_threshold"]
            })
        
        return {
            "success": True,
            "data": {
                "tariffs": tariffs,
                "profit_update_interval": PROFIT_UPDATE_INTERVAL
            },
            "message": "Список тарифов получен успешно"
        }
        
    except Exception as e:
        print(f"❌ Ошибка получения тарифов: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка получения тарифов: {str(e)}")

# API роуты для работы с балансом
@app.post("/api/balance/add")
def add_user_balance(stake_request: StakeRequest):
    """Пополнение основного баланса пользователя"""
    try:
        result = add_balance(stake_request.telegram_id, stake_request.amount, 'dep')
        return result
        
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"❌ Ошибка пополнения баланса: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка пополнения баланса: {str(e)}")

@app.post("/api/balance/withdraw")
def withdraw_user_balance(stake_request: StakeRequest):
    """Вывод средств с основного баланса пользователя"""
    try:
        result = withdraw_balance(stake_request.telegram_id, stake_request.amount, 'withdraw')
        return result
        
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"❌ Ошибка вывода средств: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка вывода средств: {str(e)}")

@app.post("/api/balance/referral-bonus")
def add_referral_bonus(stake_request: StakeRequest):
    """Начисление реферального бонуса"""
    try:
        result = add_balance(stake_request.telegram_id, stake_request.amount, 'dep_ref')
        return result
        
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"❌ Ошибка начисления реферального бонуса: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка начисления реферального бонуса: {str(e)}")

# API роуты для денежных логов
@app.get("/api/money-log/history")
def get_money_log_history(telegram_id: int, limit: int = 50, offset: int = 0):
    """Получение истории денежных операций пользователя"""
    try:
        # Проверяем параметры
        if limit < 1 or limit > 100:
            limit = 50  # Ограничиваем лимит разумными пределами
        
        if offset < 0:
            offset = 0
        
        # Получаем историю операций
        logs = get_money_logs_by_telegram_id(telegram_id, limit, offset)
        total_count = get_money_logs_count_by_telegram_id(telegram_id)
        
        return {
            "success": True,
            "data": {
                "logs": logs,
                "total_count": total_count,
                "limit": limit,
                "offset": offset,
                "has_more": (offset + limit) < total_count
            },
            "message": "История операций получена успешно"
        }
        
    except Exception as e:
        print(f"❌ Ошибка получения истории операций: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка получения истории операций: {str(e)}")

# API роуты для работы с пополнениями
@app.post("/api/deposit/create")
def create_deposit_endpoint(deposit_data: DepositRequest):
    """Создание запроса на пополнение баланса"""
    try:
        result = create_deposit_request_in_db(
            telegram_id=deposit_data.telegram_id,
            amount=deposit_data.amount,
            payment_type=deposit_data.payment_type,
            payment_details=deposit_data.payment_details
        )
        
        return {
            "success": True,
            "data": result,
            "message": "Запрос на пополнение успешно создан"
        }
        
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"❌ Ошибка создания запроса на пополнение: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка создания запроса: {str(e)}")

@app.get("/api/deposit/status/{request_id}")
def get_deposit_status_endpoint(request_id: int):
    """Получение статуса запроса на пополнение"""
    try:
        result = get_deposit_request_by_id(request_id)
        
        return {
            "success": True,
            "data": result,
            "message": "Статус получен успешно"
        }
        
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"❌ Ошибка получения статуса: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка получения статуса: {str(e)}")

@app.get("/api/deposit/last/{telegram_id}")
def get_last_deposit_endpoint(telegram_id: int):
    """Получение последнего запроса на пополнение пользователя"""
    try:
        result = get_last_deposit_request_by_telegram_id(telegram_id)
        
        if result:
            return {
                "success": True,
                "data": result,
                "message": "Последний запрос получен"
            }
        else:
            return {
                "success": False,
                "data": None,
                "message": "Запросы не найдены"
            }
        
    except Exception as e:
        print(f"❌ Ошибка получения последнего запроса: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка получения запроса: {str(e)}")

@app.post("/api/deposit/approve")
def approve_deposit_endpoint(approval_data: DepositApproval):
    """Подтверждение или отклонение запроса на пополнение (для админов)"""
    try:
        if approval_data.approved:
            result = approve_deposit_request(approval_data.request_id, approval_data.admin_id)
        else:
            result = reject_deposit_request(approval_data.request_id, approval_data.admin_id)
        
        return result
        
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"❌ Ошибка обработки запроса: {e}")
        raise HTTPException(status_code=500, detail=f"Ошибка обработки запроса: {str(e)}")

@app.get("/api/database/test")
def test_database_connection():
    """Тестирование подключения к базе данных"""
    connection = get_db_connection()
    
    if not connection:
        return {
            "success": False,
            "message": "Ошибка подключения к базе данных",
            "config": {
                "host": DB_HOST,
                "port": DB_PORT,
                "database": DB_NAME,
                "user": DB_USERNAME
            }
        }
    
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()[0]
        
        # Проверяем существование таблицы users
        cursor.execute("SHOW TABLES LIKE 'users'")
        table_exists = cursor.fetchone() is not None
        
        return {
            "success": True,
            "message": "Подключение к базе данных успешно",
            "mysql_version": version,
            "users_table_exists": table_exists,
            "config": {
                "host": DB_HOST,
                "port": DB_PORT,
                "database": DB_NAME,
                "user": DB_USERNAME
            }
        }
        
    except Error as e:
        return {
            "success": False,
            "message": f"Ошибка выполнения запроса: {str(e)}"
        }
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Добавляем отладочную информацию
@app.get("/debug/files")
def debug_files():
    """Отладка - список файлов"""
    if os.path.exists(STATIC_DIR):
        files = []
        for root, dirs, filenames in os.walk(STATIC_DIR):
            for filename in filenames:
                rel_path = os.path.relpath(os.path.join(root, filename), STATIC_DIR)
                files.append(rel_path)
        return {"static_dir": STATIC_DIR, "files": files}
    return {"error": "Static directory not found"}

@app.get("/debug/table/users")
def debug_users_table():
    """Проверка структуры таблицы users"""
    connection = get_db_connection()
    if not connection:
        return {"error": "Не удалось подключиться к базе данных"}
    
    try:
        cursor = connection.cursor()
        
        # Получаем структуру таблицы
        cursor.execute("DESCRIBE users")
        columns = cursor.fetchall()
        
        # Проверяем существование таблицы
        cursor.execute("SHOW TABLES LIKE 'users'")
        table_exists = cursor.fetchone() is not None
        
        return {
            "table_exists": table_exists,
            "columns": [{"field": col[0], "type": col[1], "null": col[2], "key": col[3], "default": col[4], "extra": col[5]} for col in columns] if table_exists else [],
            "message": "Структура таблицы получена" if table_exists else "Таблица не существует"
        }
        
    except Error as e:
        return {"error": f"Ошибка выполнения запроса: {str(e)}"}
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.post("/debug/table/users/fix")
def fix_users_table():
    """Исправление структуры таблицы users - добавление недостающих колонок"""
    connection = get_db_connection()
    if not connection:
        return {"error": "Не удалось подключиться к базе данных"}
    
    try:
        cursor = connection.cursor()
        
        # Проверяем существование таблицы
        cursor.execute("SHOW TABLES LIKE 'users'")
        if not cursor.fetchone():
            # Создаем таблицу с нуля
            create_table_query = """
                CREATE TABLE users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
                    XP VARCHAR(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '0/100',
                    telegram_ID VARCHAR(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
                    balance VARCHAR(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '0.00',
                    stake_balance VARCHAR(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '0.00',
                    profit_all VARCHAR(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '0.00',
                    partners_balance VARCHAR(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '0.00',
                    ref VARCHAR(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
                    create_accaunt DATETIME(6) NULL,
                    INDEX idx_telegram_id (telegram_ID)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
            """
            cursor.execute(create_table_query)
            connection.commit()
            return {"success": True, "message": "Таблица users создана с правильной структурой"}
        
        # Проверяем наличие колонки partners_balance
        cursor.execute("SHOW COLUMNS FROM users LIKE 'partners_balance'")
        if not cursor.fetchone():
            # Добавляем недостающую колонку
            cursor.execute("ALTER TABLE users ADD COLUMN partners_balance VARCHAR(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '0.00' AFTER profit_all")
            connection.commit()
            return {"success": True, "message": "Колонка partners_balance добавлена"}
        
        return {"success": True, "message": "Структура таблицы корректна"}
        
    except Error as e:
        connection.rollback()
        return {"error": f"Ошибка исправления структуры: {str(e)}"}
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.get("/debug/table/money_log")
def debug_money_log_table():
    """Проверка структуры таблицы money_log"""
    connection = get_db_connection()
    if not connection:
        return {"error": "Не удалось подключиться к базе данных"}
    
    try:
        cursor = connection.cursor()
        
        # Проверяем существование таблицы
        cursor.execute("SHOW TABLES LIKE 'money_log'")
        table_exists = cursor.fetchone() is not None
        
        if table_exists:
            # Получаем структуру таблицы
            cursor.execute("DESCRIBE money_log")
            columns = cursor.fetchall()
            
            return {
                "table_exists": True,
                "columns": [{"field": col[0], "type": col[1], "null": col[2], "key": col[3], "default": col[4], "extra": col[5]} for col in columns],
                "message": "Структура таблицы получена"
            }
        else:
            return {
                "table_exists": False,
                "columns": [],
                "message": "Таблица не существует"
            }
        
    except Error as e:
        return {"error": f"Ошибка выполнения запроса: {str(e)}"}
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.post("/debug/table/money_log/create")
def create_money_log_table():
    """Создание таблицы money_log"""
    connection = get_db_connection()
    if not connection:
        return {"error": "Не удалось подключиться к базе данных"}
    
    try:
        cursor = connection.cursor()
        
        # Проверяем существование таблицы
        cursor.execute("SHOW TABLES LIKE 'money_log'")
        if cursor.fetchone():
            return {"success": False, "message": "Таблица money_log уже существует"}
        
        # Создаем таблицу money_log
        create_table_query = """
            CREATE TABLE money_log (
                id INT AUTO_INCREMENT PRIMARY KEY,
                telegram_id VARCHAR(255) NOT NULL,
                action VARCHAR(50) NOT NULL,
                amount DECIMAL(15,6) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                INDEX idx_telegram_id (telegram_id),
                INDEX idx_created_at (created_at),
                INDEX idx_action (action)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """
        
        cursor.execute(create_table_query)
        connection.commit()
        
        return {"success": True, "message": "Таблица money_log создана успешно"}
        
    except Error as e:
        connection.rollback()
        return {"error": f"Ошибка создания таблицы: {str(e)}"}
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.post("/debug/table/deposit_requests/create")
def create_deposit_requests_table():
    """Создание таблицы deposit_requests"""
    connection = get_db_connection()
    if not connection:
        return {"error": "Не удалось подключиться к базе данных"}
    
    try:
        cursor = connection.cursor()
        
        # Проверяем существование таблицы
        cursor.execute("SHOW TABLES LIKE 'deposit_requests'")
        if cursor.fetchone():
            return {"success": False, "message": "Таблица deposit_requests уже существует"}
        
        # Создаем таблицу deposit_requests
        create_table_query = """
            CREATE TABLE deposit_requests (
                id INT AUTO_INCREMENT PRIMARY KEY,
                telegram_id VARCHAR(255) NOT NULL,
                username VARCHAR(255) NULL,
                amount DECIMAL(15,2) NOT NULL,
                bonus_amount DECIMAL(15,2) DEFAULT 0.00,
                total_amount DECIMAL(15,2) NOT NULL,
                payment_type VARCHAR(50) DEFAULT 'СБП',
                payment_details TEXT NULL,
                status VARCHAR(20) DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                processed_at TIMESTAMP NULL,
                processed_by VARCHAR(255) NULL,
                INDEX idx_telegram_id (telegram_id),
                INDEX idx_status (status),
                INDEX idx_created_at (created_at)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """
        
        cursor.execute(create_table_query)
        connection.commit()
        
        return {"success": True, "message": "Таблица deposit_requests создана успешно"}
        
    except Error as e:
        connection.rollback()
        return {"error": f"Ошибка создания таблицы: {str(e)}"}
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.post("/debug/table/notifications_queue/create")
def create_notifications_queue_table():
    """Создание таблицы notifications_queue"""
    connection = get_db_connection()
    if not connection:
        return {"error": "Не удалось подключиться к базе данных"}
    
    try:
        cursor = connection.cursor()
        
        # Проверяем существование таблицы
        cursor.execute("SHOW TABLES LIKE 'notifications_queue'")
        if cursor.fetchone():
            return {"success": False, "message": "Таблица notifications_queue уже существует"}
        
        # Создаем таблицу notifications_queue
        create_table_query = """
            CREATE TABLE notifications_queue (
                id INT AUTO_INCREMENT PRIMARY KEY,
                type VARCHAR(50) NOT NULL,
                data TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                processed TINYINT(1) DEFAULT 0,
                INDEX idx_processed (processed),
                INDEX idx_created_at (created_at)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """
        
        cursor.execute(create_table_query)
        connection.commit()
        
        return {"success": True, "message": "Таблица notifications_queue создана успешно"}
        
    except Error as e:
        connection.rollback()
        return {"error": f"Ошибка создания таблицы: {str(e)}"}
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.get("/api/notifications/pending")
def get_pending_notifications():
    """Получение необработанных уведомлений из очереди (для бота)"""
    connection = get_db_connection()
    if not connection:
        return {"success": False, "data": []}
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        query = """
            SELECT id, type, data, created_at
            FROM notifications_queue
            WHERE processed = 0
            ORDER BY created_at ASC
            LIMIT 100
        """
        
        cursor.execute(query)
        notifications = cursor.fetchall()
        
        result = []
        for notif in notifications:
            result.append({
                "id": notif['id'],
                "type": notif['type'],
                "data": json.loads(notif['data']) if notif['data'] else {},
                "created_at": notif['created_at'].isoformat() if notif['created_at'] else None
            })
        
        return {
            "success": True,
            "data": result,
            "count": len(result)
        }
        
    except Error as e:
        print(f"❌ Ошибка получения уведомлений: {e}")
        return {"success": False, "data": [], "error": str(e)}
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.delete("/api/notifications/{notification_id}")
def mark_notification_processed(notification_id: int):
    """Отмечает уведомление как обработанное"""
    connection = get_db_connection()
    if not connection:
        return {"success": False}
    
    try:
        cursor = connection.cursor()
        
        cursor.execute("""
            UPDATE notifications_queue
            SET processed = 1
            WHERE id = %s
        """, (notification_id,))
        
        connection.commit()
        
        return {"success": True}
        
    except Error as e:
        print(f"❌ Ошибка отметки уведомления: {e}")
        connection.rollback()
        return {"success": False, "error": str(e)}
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# =============================================
# LIVE TRANSACTIONS API
# =============================================

@app.get("/api/transactions/live")
def get_live_transactions(limit: int = 20):
    """Получение последних транзакций для отображения в live-feed"""
    connection = get_db_connection()
    if not connection:
        return {"success": False, "data": [], "error": "Database connection failed"}
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Получаем последние транзакции из money_log
        cursor.execute("""
            SELECT 
                ml.id,
                ml.telegram_id,
                ml.amount,
                ml.created_at,
                u.username
            FROM money_log ml
            LEFT JOIN users u ON ml.telegram_id = u.telegram_id
            WHERE ml.amount != 0
            ORDER BY ml.created_at DESC
            LIMIT %s
        """, (limit,))
        
        money_logs = cursor.fetchall()
        
        # Преобразуем в нужный формат
        transactions = []
        
        # Криптовалютные иконки и цвета
        crypto_data = {
            'СБП': {
                'icon': '/icon/sbp2.svg',
                'color': 'rgb(0, 176, 219)',
                'name': 'СБП'
            },
            'TON': {
                'icon': '/icon/ton.svg', 
                'color': 'rgb(0, 176, 219)',
                'name': 'TON'
            },
            'ETH': {
                'icon': '/icon/eth.svg',
                'color': 'rgb(17, 192, 167)', 
                'name': 'ETH'
            },
            'BTC': {
                'icon': '/icon/btc.svg',
                'color': 'rgb(247, 147, 26)',
                'name': 'BTC'
            },  
            'USDT': {
                'icon': '/icon/teher.webp',
                'color': 'rgb(115, 93, 237)',
                'name': 'USDT'
            }
        }
        
        for log in money_logs:
            # Определяем тип транзакции по сумме
            amount_value = float(log['amount'])
            transaction_type = "deposit" if amount_value > 0 else "withdrawal"
            
            # Используем случайный выбор криптовалюты для разнообразия
            import random
            crypto_names = ['СБП', 'TON', 'ETH', 'BTC', 'USDT']
            # Используем ID транзакции как seed для стабильности
            random.seed(log['id'])
            crypto_name = random.choice(crypto_names)
            
            crypto_info = crypto_data.get(crypto_name, crypto_data['СБП'])
            
            # Форматируем время
            created_time = log['created_at']
            time_str = created_time.strftime('%H:%M:%S') if created_time else '00:00:00'
            
            # Форматируем сумму
            amount_formatted = f"+{int(abs(amount_value))}₽" if amount_value > 0 else f"-{int(abs(amount_value))}₽"
            
            transactions.append({
                "id": f"log_{log['id']}",
                "type": transaction_type,
                "typeText": "Пополнение" if transaction_type == "deposit" else "Вывод средств",
                "borderColor": crypto_info['color'],
                "cryptoName": crypto_info['name'],
                "cryptoClass": "",
                "cryptoIcon": crypto_info['icon'],
                "time": time_str,
                "amount": amount_formatted,
                "username": log['username'] or "Аноним",
                "telegram_id": log['telegram_id'],
                "timestamp": created_time.timestamp() if created_time else 0
            })
        
        return {
            "success": True,
            "data": transactions,
            "total": len(transactions)
        }
        
    except Error as e:
        print(f"❌ Ошибка получения live транзакций: {e}")
        return {"success": False, "data": [], "error": str(e)}
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.get("/api/transactions/stats")
def get_transaction_stats():
    """Получение статистики транзакций"""
    connection = get_db_connection()
    if not connection:
        return {"success": False, "error": "Database connection failed"}
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Общая статистика пополнений за сегодня (положительные суммы)
        cursor.execute("""
            SELECT 
                COUNT(*) as total_deposits,
                COALESCE(SUM(amount), 0) as total_amount,
                COALESCE(AVG(amount), 0) as avg_amount
            FROM money_log 
            WHERE amount > 0 
            AND DATE(created_at) = CURDATE()
        """)
        
        today_deposits = cursor.fetchone()
        
        # Статистика выводов за сегодня (отрицательные суммы)
        cursor.execute("""
            SELECT 
                COUNT(*) as total_withdrawals,
                COALESCE(SUM(ABS(amount)), 0) as total_amount
            FROM money_log 
            WHERE amount < 0 
            AND DATE(created_at) = CURDATE()
        """)
        
        today_withdrawals = cursor.fetchone()
        
        # Статистика за последний час
        cursor.execute("""
            SELECT 
                COUNT(*) as recent_count,
                COUNT(CASE WHEN amount > 0 THEN 1 END) as recent_deposits,
                COUNT(CASE WHEN amount < 0 THEN 1 END) as recent_withdrawals
            FROM money_log 
            WHERE amount != 0
            AND created_at >= DATE_SUB(NOW(), INTERVAL 1 HOUR)
        """)
        
        recent_stats = cursor.fetchone()
        
        return {
            "success": True,
            "data": {
                "today": {
                    "total_deposits": today_deposits['total_deposits'],
                    "total_withdrawals": today_withdrawals['total_withdrawals'],
                    "deposits_amount": float(today_deposits['total_amount']),
                    "withdrawals_amount": float(today_withdrawals['total_amount']),
                    "avg_deposit": float(today_deposits['avg_amount'])
                },
                "last_hour": {
                    "total_count": recent_stats['recent_count'],
                    "deposits_count": recent_stats['recent_deposits'],
                    "withdrawals_count": recent_stats['recent_withdrawals']
                }
            }
        }
        
    except Error as e:
        print(f"❌ Ошибка получения статистики транзакций: {e}")
        return {"success": False, "error": str(e)}
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# =============================================
# DEBUG ENDPOINTS для тестирования live транзакций
# =============================================

@app.post("/debug/transactions/add-test")
def add_test_transaction(transaction_type: str = "deposit", amount: float = 1000, crypto: str = "СБП"):
    """Добавление тестовой транзакции в money_log"""
    connection = get_db_connection()
    if not connection:
        return {"success": False, "error": "Database connection failed"}
    
    try:
        cursor = connection.cursor()
        
        # Определяем сумму в зависимости от типа транзакции
        final_amount = amount if transaction_type == "deposit" else -amount
        
        # Используем тестовый telegram_id (851069605)
        test_telegram_id = 851069605
        
        # Добавляем запись в money_log (без поля message, которого нет в таблице)
        cursor.execute("""
            INSERT INTO money_log (telegram_id, amount, created_at)
            VALUES (%s, %s, NOW())
        """, (test_telegram_id, final_amount))
        
        connection.commit()
        
        return {
            "success": True,
            "message": f"Тестовая транзакция добавлена",
            "data": {
                "type": transaction_type,
                "amount": final_amount,
                "crypto": crypto,
                "telegram_id": test_telegram_id
            }
        }
        
    except Error as e:
        print(f"❌ Ошибка добавления тестовой транзакции: {e}")
        connection.rollback()
        return {"success": False, "error": str(e)}
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.post("/debug/transactions/add-random")
def add_random_transactions(count: int = 5):
    """Добавление случайных тестовых транзакций"""
    import random
    
    cryptos = ['СБП', 'TON', 'ETH', 'BTC', 'USDT']
    transaction_types = ['deposit', 'withdrawal']
    
    results = []
    
    for i in range(count):
        crypto = random.choice(cryptos)
        trans_type = random.choice(transaction_types)
        amount = random.randint(100, 5000)
        
        result = add_test_transaction(trans_type, amount, crypto)
        results.append(result)
    
    successful = sum(1 for r in results if r.get('success', False))
    
    return {
        "success": True,
        "message": f"Создано {successful} из {count} тестовых транзакций",
        "results": results
    }
