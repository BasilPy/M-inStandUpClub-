from aiogram import Bot, Dispatcher, executor, types

TOKEN = "5639207346:AAGBiSMzngJM35OOqEH9RXcHf8waAYp3M24"


async def welcome(message: types.Message):
    # gspread_test.new_line_client()
    await message.reply("Hello! This is Mәin standUp Club \nfrom Almaty")


def register_handlers_client(_dispatcher: Dispatcher):
    _dispatcher.register_message_handler(welcome, commands=['start', 'help'])


async def on_startup(_):
    print("Bot stated!")


if __name__ == '__main__':
    bot = Bot(token=TOKEN)
    dispatcher = Dispatcher(bot)
    register_handlers_client(dispatcher)
    executor.start_polling(dispatcher, on_startup=on_startup)

