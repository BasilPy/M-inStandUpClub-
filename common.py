from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from menu.main_menu import menu
from menu.models import MenuItem, MultiLangText, MenuCategory, ShoppingBasket
from menu.basket import basket


def _create_button(menu_item: MenuItem, lang) -> InlineKeyboardButton:
    text = menu_item.name.__getattribute__(lang)
    button = InlineKeyboardButton(text=text, callback_data=menu_item.item_id)
    return button


def get_exact_category(category_name) -> MenuCategory:
    for category in menu.categories:
        if category_name == category.item_id:
            return category


def get_title_of_categories(lang):
    return menu.title_categories.get_text_by_language(lang)


def get_title_of_category_items(call, lang):
    return get_exact_category(category_name=call.data).instruction.get_text_by_language(lang)



def get_category_items_markup(category: MenuCategory, lang: str) -> InlineKeyboardMarkup:
    category_items = get_exact_category(category).category_items
    buttons = [
        _create_button(menu_item=category_item, lang=lang) for category_item in category_items
    ]
    markup = InlineKeyboardMarkup()
    for button in buttons:
        markup.add(button)
    return markup


def get_categories_markup(lang: str) -> InlineKeyboardMarkup:
    buttons = [
        _create_button(menu_item=category, lang=lang) for category in menu.categories
    ]
    markup = InlineKeyboardMarkup()
    for button in buttons:
        markup.row(button)
    return markup


def get_basket_markup(lang: str) -> InlineKeyboardMarkup:
    buttons = [
        _create_button(menu_item=category_item, lang=lang) for category_item in basket.items_in_basket
    ]
    markup = InlineKeyboardMarkup()
    for button in buttons:
        markup.add(button)
    return markup