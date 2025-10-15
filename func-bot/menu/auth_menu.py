from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_auth_keyboard(channel_link: str):
    """
    Создает инлайн клавиатуру для авторизации
    :param channel_link: ссылка на канал из конфига
    :return: InlineKeyboardMarkup
    """
    keyboard = InlineKeyboardBuilder()
    
    # Кнопка "Вступить в форум" - открывает ссылку из конфига
    keyboard.add(InlineKeyboardButton(
        text="➕Вступить в форум",
        url=channel_link
    ))
    
    # Кнопка "Продолжить" - пока callback без действий
    keyboard.add(InlineKeyboardButton(
        text="✔️Продолжить", 
        callback_data="continue"
    ))
    
    # Размещение кнопок в два ряда
    keyboard.adjust(1)
    
    return keyboard.as_markup()







