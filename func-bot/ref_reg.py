"""
Модуль для работы с реферальной системой
Обрабатывает регистрацию пользователей по реферальным ссылкам
"""

import logging
import re
from typing import Optional, Dict, Any
from config import BOT_TOKEN, BOT_USERNAME

logger = logging.getLogger(__name__)

def extract_ref_from_start_command(command_text: str) -> Optional[str]:
    """
    Извлекает реферальный код из команды /start
    
    Args:
        command_text (str): Полный текст команды /start
        
    Returns:
        Optional[str]: Telegram ID реферера или None
        
    Example:
        /start ref_123456789 -> "123456789"
        /start -> None
    """
    try:
        # Разбиваем команду на части
        parts = command_text.strip().split()
        
        if len(parts) < 2:
            return None
            
        # Проверяем второй параметр на соответствие формату ref_telegram_id
        ref_param = parts[1]
        
        # Паттерн для реферального кода: ref_123456789
        ref_pattern = r'^ref_(\d+)$'
        match = re.match(ref_pattern, ref_param)
        
        if match:
            telegram_id = match.group(1)
            logger.info(f"🔗 Извлечен реферальный код: {telegram_id}")
            return telegram_id
        else:
            logger.info(f"⚠️ Неверный формат реферального кода: {ref_param}")
            return None
            
    except Exception as e:
        logger.error(f"❌ Ошибка извлечения реферального кода: {e}")
        return None

def generate_referral_link(bot_username: str, telegram_id: int) -> str:
    """
    Генерирует реферальную ссылку для пользователя
    
    Args:
        bot_username (str): Username бота (без @)
        telegram_id (int): Telegram ID пользователя
        
    Returns:
        str: Готовая реферальная ссылка
        
    Example:
        generate_referral_link("RoyallAppBot", 123456789) 
        -> "https://t.me/RoyallAppBot?start=ref_123456789"
    """
    try:
        # Убираем @ если он есть
        clean_username = bot_username.lstrip('@')
        
        # Формируем ссылку
        ref_link = f"https://t.me/{clean_username}?start=ref_{telegram_id}"
        
        logger.info(f"🔗 Сгенерирована реферальная ссылка для {telegram_id}: {ref_link}")
        return ref_link
        
    except Exception as e:
        logger.error(f"❌ Ошибка генерации реферальной ссылки: {e}")
        return f"https://t.me/{bot_username}?start=ref_{telegram_id}"

def validate_referrer_id(referrer_id: str, new_user_id: int) -> bool:
    """
    Проверяет валидность реферера
    
    Args:
        referrer_id (str): Telegram ID реферера
        new_user_id (int): Telegram ID нового пользователя
        
    Returns:
        bool: True если реферер валиден, False если нет
    """
    try:
        # Проверяем, что это числовое значение
        referrer_telegram_id = int(referrer_id)
        
        # Пользователь не может быть реферером самого себя
        if referrer_telegram_id == new_user_id:
            logger.warning(f"⚠️ Пользователь {new_user_id} пытается стать реферером самого себя")
            return False
            
        # Проверяем, что ID выглядит как Telegram ID (больше 0)
        if referrer_telegram_id <= 0:
            logger.warning(f"⚠️ Неверный Telegram ID реферера: {referrer_telegram_id}")
            return False
            
        logger.info(f"✅ Реферер {referrer_telegram_id} валиден для пользователя {new_user_id}")
        return True
        
    except ValueError:
        logger.warning(f"⚠️ Реферальный ID не является числом: {referrer_id}")
        return False
    except Exception as e:
        logger.error(f"❌ Ошибка валидации реферера: {e}")
        return False

def format_referral_info(referrer_id: str, new_user_info: Dict[str, Any]) -> Dict[str, Any]:
    """
    Форматирует информацию о реферальной регистрации для логов и API
    
    Args:
        referrer_id (str): Telegram ID реферера  
        new_user_info (Dict): Информация о новом пользователе
        
    Returns:
        Dict: Отформатированная информация
    """
    try:
        return {
            "referrer_telegram_id": int(referrer_id),
            "new_user_telegram_id": new_user_info.get("telegram_id"),
            "new_user_username": new_user_info.get("username"),
            "registration_type": "referral",
            "referral_link": f"ref_{referrer_id}",
            "timestamp": new_user_info.get("created_at")
        }
    except Exception as e:
        logger.error(f"❌ Ошибка форматирования реферальной информации: {e}")
        return {
            "referrer_telegram_id": referrer_id,
            "new_user_telegram_id": new_user_info.get("telegram_id"),
            "registration_type": "referral_error",
            "error": str(e)
        }

def get_bot_username_from_token(token: str) -> str:
    """
    Извлекает username бота из токена (если возможно) или возвращает дефолтное имя
    
    Args:
        token (str): Токен бота
        
    Returns:
        str: Username бота
    """
    try:
        # В реальной ситуации можно было бы сделать API запрос к Telegram
        # Но для простоты возвращаем дефолтное имя
        # TODO: Можно добавить получение имени через Bot API
        return BOT_USERNAME  # Имя бота из конфигурации
        
    except Exception as e:
        logger.error(f"❌ Ошибка получения username бота: {e}")
        return "RoyallAppBot"

def log_referral_registration(referrer_id: str, new_user_info: Dict[str, Any], success: bool = True):
    """
    Логирует реферальную регистрацию
    
    Args:
        referrer_id (str): ID реферера
        new_user_info (Dict): Информация о новом пользователе
        success (bool): Успешность регистрации
    """
    try:
        if success:
            logger.info(
                f"✅ РЕФЕРАЛЬНАЯ РЕГИСТРАЦИЯ: "
                f"Пользователь {new_user_info.get('username')} (ID: {new_user_info.get('telegram_id')}) "
                f"зарегистрирован по ссылке реферера {referrer_id}"
            )
        else:
            logger.warning(
                f"⚠️ ОШИБКА РЕФЕРАЛЬНОЙ РЕГИСТРАЦИИ: "
                f"Пользователь {new_user_info.get('username')} (ID: {new_user_info.get('telegram_id')}) "
                f"не смог зарегистрироваться по ссылке реферера {referrer_id}"
            )
    except Exception as e:
        logger.error(f"❌ Ошибка логирования реферальной регистрации: {e}")

# Константы для реферальной системы
REFERRAL_PREFIX = "ref_"
REFERRAL_REWARD_AMOUNT = 10.0  # Награда за реферала
REFERRAL_MIN_ID_LENGTH = 6     # Минимальная длина Telegram ID

def calculate_referral_reward(referrer_level: int = 1) -> float:
    """
    Рассчитывает награду за реферала в зависимости от уровня реферера
    
    Args:
        referrer_level (int): Уровень реферера
        
    Returns:
        float: Размер награды
    """
    base_reward = REFERRAL_REWARD_AMOUNT
    
    # Можно добавить бонусы за уровень
    level_bonus = (referrer_level - 1) * 2.0
    
    return base_reward + level_bonus
