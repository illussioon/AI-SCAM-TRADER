import random
import time
import math
import sys
import os

# Добавляем путь к конфигам
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'configs'))
from config import FAKE_ONLINE_DIAPASON_MIN, FAKE_ONLINE_DIAPASON_MAX, ONLINE_UPDATE_DELAY

def smooth_online_generator(min_users=FAKE_ONLINE_DIAPASON_MIN, max_users=FAKE_ONLINE_DIAPASON_MAX, step_delay=ONLINE_UPDATE_DELAY):
    """
    Генерирует реалистичные изменения онлайна с ростом и падениями.
    :param min_users: минимальное значение онлайна
    :param max_users: максимальное значение онлайна
    :param step_delay: пауза между обновлениями (в секундах)
    """
    # Текущее значение — начинаем со случайной точки
    current_online = random.randint(min_users, max_users)
    
    # Параметры тренда (общее направление движения)
    trend_direction = random.choice([-1, 1])  # -1 = падение, 1 = рост
    trend_strength = random.uniform(0.3, 0.8)  # сила тренда
    trend_duration = random.randint(5, 15)  # сколько шагов продлится тренд
    trend_counter = 0
    
    # Параметры для плавной волны
    phase = random.random() * math.pi * 2
    
    # Параметры для резких скачков (имитация событий)
    spike_probability = 0.05  # 5% шанс резкого изменения
    
    while True:
        # Смена тренда через определённое время
        trend_counter += 1
        if trend_counter >= trend_duration:
            trend_direction = random.choice([-1, 1])
            trend_strength = random.uniform(0.3, 0.8)
            trend_duration = random.randint(5, 15)
            trend_counter = 0
        
        # Основной тренд (рост или падение)
        trend_change = trend_direction * trend_strength * random.uniform(0.5, 1.5)
        
        # Плавная волна (суточные колебания)
        wave = math.sin(phase) * (max_users - min_users) * 0.03
        phase += random.uniform(0.08, 0.12)
        
        # Малые случайные флуктуации
        noise = random.uniform(-5, 5)
        
        # Случайные резкие изменения (события: приход/уход группы людей)
        spike = 0
        if random.random() < spike_probability:
            spike = random.choice([-1, 1]) * random.uniform(10, 30)
        
        # Суммарное изменение
        total_change = trend_change + wave + noise + spike
        current_online += total_change
        
        # Ограничиваем в пределах диапазона с эффектом отскока
        if current_online < min_users:
            current_online = min_users + random.uniform(5, 20)
            trend_direction = 1  # разворачиваем тренд вверх
            trend_counter = 0
        elif current_online > max_users:
            current_online = max_users - random.uniform(5, 20)
            trend_direction = -1  # разворачиваем тренд вниз
            trend_counter = 0
        
         # Добавляем естественную неровность (не всегда целое число)
         display_online = int(current_online + random.uniform(-1, 1))
         
         print(display_online)
        
        # Задержка между обновлениями с небольшой вариацией
        actual_delay = step_delay * random.uniform(0.9, 1.1)
        time.sleep(actual_delay)


# Запуск скрипта при прямом вызове
if __name__ == "__main__":
    smooth_online_generator()