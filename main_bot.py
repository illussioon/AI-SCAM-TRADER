import asyncio
import logging
import sys
import os

# Добавляем путь к модулям бота
sys.path.append(os.path.join(os.path.dirname(__file__), 'func-bot'))

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import FSInputFile
import aiohttp
import json
from config import BOT_TOKEN, CHANNEL_LINKS, BOT_USERNAME, ADMIN_IDS
from menu.auth_menu import get_auth_keyboard
from start_api import start_api_in_thread
from ref_reg import (
    extract_ref_from_start_command, 
    validate_referrer_id, 
    generate_referral_link,
    get_bot_username_from_token,
    log_referral_registration,
    format_referral_info
)

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Создание экземпляров бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# API сервер URL
API_BASE_URL = "http://127.0.0.1:8000"

async def notify_referrer_about_new_user(referrer_telegram_id: str, new_username: str):
    """Уведомляет реферера о новом пользователе"""
    try:
        notification_text = (
            f"🎉 Поздравляем!\n\n"
            f"👤 Пользователь {new_username} присоединился по вашей реферальной ссылке!\n"
            f"💰 Вам начислена награда за реферала!"
        )
        
        await bot.send_message(
            chat_id=int(referrer_telegram_id),
            text=notification_text
        )
        
        logger.info(f"✅ Уведомление отправлено рефереру {referrer_telegram_id}")
        
    except Exception as e:
        logger.error(f"❌ Ошибка отправки уведомления рефереру {referrer_telegram_id}: {e}")

async def create_user_via_api(username: str, telegram_id: int, ref: str = None) -> dict:
    """Создает пользователя через API сервер"""
    try:
        user_data = {
            "username": username,
            "telegram_id": telegram_id,
            "ref": ref
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{API_BASE_URL}/api/user/create",
                json=user_data,
                headers={"Content-Type": "application/json"}
            ) as response:
                
                if response.status == 200:
                    result = await response.json()
                    logger.info(f"✅ API ответ создания пользователя: {result}")
                    return result
                else:
                    error_text = await response.text()
                    logger.error(f"❌ Ошибка API создания пользователя: {response.status} - {error_text}")
                    return {"success": False, "error": f"HTTP {response.status}"}
                    
    except Exception as e:
        logger.error(f"❌ Исключение при создании пользователя: {e}")
        return {"success": False, "error": str(e)}

async def notify_admins_about_deposit(request_data: dict):
    """Уведомляет администраторов о новом запросе на пополнение"""
    try:
        request_id = request_data['request_id']
        telegram_id = request_data['telegram_id']
        username = request_data.get('username', 'Неизвестно')
        amount = request_data['amount']
        bonus_amount = request_data['bonus_amount']
        total_amount = request_data['total_amount']
        payment_type = request_data['payment_type']
        
        # Формируем сообщение для админов
        message_text = (
            f"💰 <b>Новое пополнение</b>\n\n"
            f"<b>Тип операции:</b> {payment_type}\n"
            f"<b>Сумма:</b> {amount}₽\n"
            f"<b>Сумма с учётом бонусов:</b> {total_amount}₽\n"
            f"<b>Бонус:</b> +{bonus_amount}₽ ({int((bonus_amount/amount)*100)}%)\n\n"
            f"<b>User ID:</b> <code>{telegram_id}</code>\n"
            f"<b>Username:</b> @{username}\n\n"
            f"<i>Запрос ID: {request_id}</i>"
        )
        
        # Создаем inline клавиатуру с кнопками
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✅ Подтвердить пополнение",
                    callback_data=f"deposit_approve_{request_id}"
                )
            ],
            [
                InlineKeyboardButton(
                    text="❌ Отклонить пополнение",
                    callback_data=f"deposit_reject_{request_id}"
                )
            ]
        ])
        
        # Отправляем сообщение всем админам
        for admin_id in ADMIN_IDS:
            try:
                await bot.send_message(
                    chat_id=admin_id,
                    text=message_text,
                    reply_markup=keyboard,
                    parse_mode="HTML"
                )
                logger.info(f"✅ Уведомление о пополнении отправлено админу {admin_id}")
            except Exception as e:
                logger.error(f"❌ Ошибка отправки уведомления админу {admin_id}: {e}")
                
    except Exception as e:
        logger.error(f"❌ Ошибка уведомления админов: {e}")

async def process_deposit_approval(request_id: int, admin_id: int, approved: bool):
    """Обрабатывает подтверждение или отклонение пополнения"""
    try:
        approval_data = {
            "request_id": request_id,
            "approved": approved,
            "admin_id": admin_id
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{API_BASE_URL}/api/deposit/approve",
                json=approval_data,
                headers={"Content-Type": "application/json"}
            ) as response:
                
                if response.status == 200:
                    result = await response.json()
                    logger.info(f"✅ Пополнение {'подтверждено' if approved else 'отклонено'}: {result}")
                    return result
                else:
                    error_text = await response.text()
                    logger.error(f"❌ Ошибка обработки пополнения: {response.status} - {error_text}")
                    return {"success": False, "error": f"HTTP {response.status}"}
                    
    except Exception as e:
        logger.error(f"❌ Исключение при обработке пополнения: {e}")
        return {"success": False, "error": str(e)}

async def notify_user_about_deposit_result(telegram_id: int, approved: bool, amount: float = 0):
    """Уведомляет пользователя о результате пополнения"""
    try:
        if approved:
            message_text = (
                f"✅ <b>Пополнение подтверждено!</b>\n\n"
                f"На ваш баланс зачислено: <b>{amount}₽</b>\n"
                f"Спасибо за использование нашего сервиса!"
            )
        else:
            message_text = (
                f"❌ <b>Пополнение отклонено</b>\n\n"
                f"К сожалению, ваш запрос на пополнение был отклонен.\n"
                f"Если у вас есть вопросы, обратитесь в поддержку."
            )
        
        await bot.send_message(
            chat_id=telegram_id,
            text=message_text,
            parse_mode="HTML"
        )
        
        logger.info(f"✅ Уведомление о результате отправлено пользователю {telegram_id}")
        
    except Exception as e:
        logger.error(f"❌ Ошибка отправки уведомления пользователю {telegram_id}: {e}")

# Обработчик callback для подтверждения пополнения
@dp.callback_query(F.data.startswith("deposit_approve_"))
async def handle_deposit_approve(callback: CallbackQuery):
    """Обрабатывает подтверждение пополнения админом"""
    try:
        # Извлекаем ID запроса из callback data
        request_id = int(callback.data.split("_")[-1])
        admin_id = callback.from_user.id
        
        # Проверяем, является ли пользователь админом
        if admin_id not in ADMIN_IDS:
            await callback.answer("❌ У вас нет прав для выполнения этой операции", show_alert=True)
            return
        
        # Обрабатываем подтверждение
        result = await process_deposit_approval(request_id, admin_id, approved=True)
        
        if result.get("success"):
            # Получаем данные из результата
            telegram_id = result['data']['telegram_id']
            credited_amount = result['data']['credited_amount']
            
            # Обновляем сообщение админа
            await callback.message.edit_text(
                f"{callback.message.text}\n\n✅ <b>ПОДТВЕРЖДЕНО</b> администратором @{callback.from_user.username}",
                reply_markup=None,
                parse_mode="HTML"
            )
            
            # Уведомляем пользователя
            await notify_user_about_deposit_result(int(telegram_id), approved=True, amount=credited_amount)
            
            await callback.answer("✅ Пополнение подтверждено!")
        else:
            await callback.answer(f"❌ Ошибка: {result.get('error', 'Неизвестная ошибка')}", show_alert=True)
            
    except Exception as e:
        logger.error(f"❌ Ошибка обработки подтверждения: {e}")
        await callback.answer(f"❌ Ошибка: {str(e)}", show_alert=True)

# Обработчик callback для отклонения пополнения
@dp.callback_query(F.data.startswith("deposit_reject_"))
async def handle_deposit_reject(callback: CallbackQuery):
    """Обрабатывает отклонение пополнения админом"""
    try:
        # Извлекаем ID запроса из callback data
        request_id = int(callback.data.split("_")[-1])
        admin_id = callback.from_user.id
        
        # Проверяем, является ли пользователь админом
        if admin_id not in ADMIN_IDS:
            await callback.answer("❌ У вас нет прав для выполнения этой операции", show_alert=True)
            return
        
        # Обрабатываем отклонение
        result = await process_deposit_approval(request_id, admin_id, approved=False)
        
        if result.get("success"):
            # Получаем данные из результата
            telegram_id = result['data']['telegram_id']
            
            # Обновляем сообщение админа
            await callback.message.edit_text(
                f"{callback.message.text}\n\n❌ <b>ОТКЛОНЕНО</b> администратором @{callback.from_user.username}",
                reply_markup=None,
                parse_mode="HTML"
            )
            
            # Уведомляем пользователя
            await notify_user_about_deposit_result(int(telegram_id), approved=False)
            
            await callback.answer("✅ Пополнение отклонено!")
        else:
            await callback.answer(f"❌ Ошибка: {result.get('error', 'Неизвестная ошибка')}", show_alert=True)
            
    except Exception as e:
        logger.error(f"❌ Ошибка обработки отклонения: {e}")
        await callback.answer(f"❌ Ошибка: {str(e)}", show_alert=True)

@dp.message(Command("start"))
async def start_command(message: Message):
    """Обработчик команды /start"""
    
    # Получаем данные пользователя
    user = message.from_user
    username = user.username or f"{user.first_name}_{user.last_name}" or f"user_{user.id}"
    telegram_id = user.id
    
    logger.info(f"🔄 Команда /start от пользователя: {username} (ID: {telegram_id})")
    
    # Пытаемся создать пользователя в базе данных
    try:
        # Извлекаем реферальный код из команды /start
        referrer_telegram_id = extract_ref_from_start_command(message.text)
        
        # Валидируем реферера, если он есть
        if referrer_telegram_id:
            if validate_referrer_id(referrer_telegram_id, telegram_id):
                logger.info(f"🔗 Валидный реферальный код от пользователя: {referrer_telegram_id}")
            else:
                logger.warning(f"⚠️ Невалидный реферальный код: {referrer_telegram_id}")
                referrer_telegram_id = None
        
        # Создаем пользователя через API
        user_creation_result = await create_user_via_api(
            username=username,
            telegram_id=telegram_id,
            ref=referrer_telegram_id
        )
        
        if user_creation_result.get("success"):
            creation_data = user_creation_result.get("data", {})
            if creation_data.get("status") == "created":
                logger.info(f"✅ Новый пользователь зарегистрирован: {username} (ID: {telegram_id})")
                
                # Логируем реферальную регистрацию, если есть реферер
                if referrer_telegram_id:
                    user_info = {
                        "telegram_id": telegram_id,
                        "username": username,
                        "created_at": creation_data.get("created_at")
                    }
                    log_referral_registration(referrer_telegram_id, user_info, success=True)
                    
                    # Можно добавить уведомление реферера
                    try:
                        await notify_referrer_about_new_user(referrer_telegram_id, username)
                    except Exception as e:
                        logger.error(f"❌ Ошибка уведомления реферера: {e}")
                        
            else:
                logger.info(f"ℹ️ Пользователь уже существует: {username} (ID: {telegram_id})")
        else:
            logger.warning(f"⚠️ Не удалось создать пользователя в БД: {user_creation_result.get('error', 'Неизвестная ошибка')}")
            
            # Логируем неудачную реферальную регистрацию
            if referrer_telegram_id:
                user_info = {
                    "telegram_id": telegram_id,
                    "username": username
                }
                log_referral_registration(referrer_telegram_id, user_info, success=False)
            
    except Exception as e:
        logger.error(f"❌ Ошибка при создании пользователя: {e}")
    
    # Текст приветственного сообщения
    welcome_text = (
        "👋 Добро пожаловать в Royal APL\n\n"
        "☑️ Для работы вступите в форум участников крипто-приложения!"
    )
    
    # Создание инлайн клавиатуры
    keyboard = get_auth_keyboard(CHANNEL_LINKS)
    
    # Путь к изображению (абсолютный путь)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    photo_path = os.path.join(current_dir, "func-bot", "img", "auth.jpg")
    photo = FSInputFile(photo_path)
    
    try:
        # Отправка фото с сообщением и клавиатурой
        await message.answer_photo(
            photo=photo,
            caption=welcome_text,
            reply_markup=keyboard
        )
    except Exception as e:
        logger.error(f"Ошибка при отправке фото: {e}")
        # В случае ошибки отправляем просто текст с кнопками
        await message.answer(
            text=welcome_text,
            reply_markup=keyboard
        )


async def check_notifications_queue():
    """Фоновая задача для проверки очереди уведомлений"""
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                # Получаем необработанные уведомления
                async with session.get(f"{API_BASE_URL}/api/notifications/pending") as response:
                    if response.status == 200:
                        result = await response.json()
                        
                        if result.get("success") and result.get("data"):
                            for notification in result['data']:
                                notif_id = notification['id']
                                notif_type = notification['type']
                                notif_data = notification['data']
                                
                                # Обрабатываем уведомление в зависимости от типа
                                if notif_type == 'deposit_request':
                                    await notify_admins_about_deposit(notif_data)
                                
                                # Отмечаем уведомление как обработанное
                                async with session.delete(f"{API_BASE_URL}/api/notifications/{notif_id}") as del_response:
                                    if del_response.status == 200:
                                        logger.info(f"✅ Уведомление {notif_id} обработано")
                                    
        except Exception as e:
            logger.error(f"❌ Ошибка проверки очереди уведомлений: {e}")
        
        # Проверяем каждые 3 секунды
        await asyncio.sleep(3)

async def main():
    """Основная функция запуска бота и API сервера"""
    print("🚀 Запуск Royal APL...")
    print("=" * 40)
    
    # Запуск API сервера в отдельном потоке
    print("🌐 Запуск API сервера...")
    api_thread = start_api_in_thread()
    
    # Небольшая задержка для запуска API
    await asyncio.sleep(3)
    
    print("🌍 Веб-интерфейс доступен: http://127.0.0.1:8000")
    print("🔍 Отладка файлов: http://127.0.0.1:8000/debug/files")
    print("=" * 40)
    
    logger.info("🤖 Запуск Telegram бота...")
    
    # Создаем фоновую задачу для проверки уведомлений
    notifications_task = asyncio.create_task(check_notifications_queue())
    
    try:
        # Запуск поллинга бота
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")
    finally:
        # Отменяем фоновую задачу
        notifications_task.cancel()
        try:
            await notifications_task
        except asyncio.CancelledError:
            pass
        
        # Закрытие сессии бота
        await bot.session.close()
        print("⏹️ Сервисы остановлены")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен пользователем")

