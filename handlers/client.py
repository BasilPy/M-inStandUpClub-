import asyncio
from aiogram import types, Dispatcher
from common import get_category_markup, get_exact_category
from menu.language_menu import keyboard_inline_1

curr_lang = "ru"


async def welcome(message: types.Message):
    await message.reply("Hello Almaty! This is Mәin standUp Club \
                        \n🗣️👅💬",
                        reply_markup=keyboard_inline_1)


async def chosen_param_language(call: types.CallbackQuery):
    global curr_lang
    curr_lang = call.data
    await call.message.answer(
        text=get_exact_category(category_name=call.data).instruction.get_text_by_language(curr_lang),
        reply_markup=get_category_markup(category=call.data, lang=curr_lang)
    )
    # if call.data == "kz":
    #     curr_lang = "kz"
    #     await call.message.answer(text="Санатты таңдаңыз:", reply_markup=keyboard_inline_menu_kz)
    # if call.data == "ru":
    #     curr_lang = "ru"
    #     await call.message.answer(text="Выберите категорию:", reply_markup=keyboard_inline_menu_ru)
    # if call.data == "eng":
    #     curr_lang = "eng"
    #     await call.message.answer(text="Chose category:", reply_markup=keyboard_inline_menu_eng)
    # await call.answer()


async def chosen_param(call: types.CallbackQuery):
    global curr_lang
    await call.message.answer(
        text=get_exact_category(category_name=call.data).instruction.get_text_by_language(curr_lang),
        reply_markup=get_category_markup(category=call.data, lang=curr_lang)
    )


def register_handlers_client(_dispatcher: Dispatcher):
    _dispatcher.register_message_handler(welcome, commands=['start', 'help'])
    _dispatcher.register_callback_query_handler(chosen_param_language, text=['kz', 'ru', 'eng'])
    _dispatcher.register_callback_query_handler(chosen_param,
                                                text=['cocktails', 'tinctures', 'beer', 'cider', 'snacks', 'wine',
                                                      'non_alcoholic'])
