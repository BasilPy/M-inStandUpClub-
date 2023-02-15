import asyncio
from aiogram import types, Dispatcher
from common import get_category_items_markup, get_exact_category, get_categories_markup
from menu.main_menu import menu
from menu.language_menu import keyboard_inline_1

curr_lang = "ru"


async def welcome_and_choose_language(message: types.Message):
    await message.reply("Hello Almaty! This is Mәin standUp Club \
                        \n🗣️👅💬",
                        reply_markup=keyboard_inline_1)


async def pass_category_by_language(call: types.CallbackQuery):
    global curr_lang
    curr_lang = call.data
    await call.message.answer(
        text="Выберите категорию:",
        reply_markup=get_categories_markup(lang=curr_lang)
    )


async def pass_items_by_category(call: types.CallbackQuery):
    global curr_lang
    await call.message.answer(
        text="Выбери!: ", # get_exact_category(category_name=call.data).instruction.get_text_by_language(curr_lang),
        reply_markup=get_category_items_markup(category=call.data, lang=curr_lang)
    )


def register_handlers_client(_dispatcher: Dispatcher):
    _dispatcher.register_message_handler(welcome_and_choose_language, commands=['start', 'help'])
    _dispatcher.register_callback_query_handler(pass_category_by_language, text=['kz', 'ru', 'eng'])
    _dispatcher.register_callback_query_handler(pass_items_by_category,
                                                text=['cocktails', 'tinctures', 'beer', 'cider', 'snacks', 'wine',
                                                      'non_alcoholic'])
