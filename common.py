from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from menu.menu import menu
from menu.models import MenuItem, MultiLangText


def _create_button(menu_item: MenuItem, lang) -> InlineKeyboardButton:
    text = menu_item.name.__getattribute__(lang)
    button = InlineKeyboardButton(text=text, callback_data=menu_item.item_id)
    return button


def get_exact_category(category_name):
    for category in menu.categories:
        if category_name == category.category_name:
            return category


def get_category_markup(category, lang) -> InlineKeyboardMarkup:
    category_items = get_exact_category(category).category_items
    buttons = [
        _create_button(menu_item=category_item, lang=lang) for category_item in category_items
    ]
    markup = InlineKeyboardMarkup()
    for button in buttons:
        markup.row(button)
    return markup

