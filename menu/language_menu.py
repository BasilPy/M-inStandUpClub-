from menu.models import Menu, MenuCategory, MultiLangText
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

language_ch = 0
button_language_1 = InlineKeyboardButton(text="Kz", callback_data="kz")
button_language_2 = InlineKeyboardButton(text="Ru", callback_data="ru")
button_language_3 = InlineKeyboardButton(text="Eng", callback_data="eng")

keyboard_inline_1 = InlineKeyboardMarkup().add(button_language_1, button_language_2, button_language_3)
