from aiogram import Bot, Dispatcher, executor, types
#from db_workspace.sqlite_db import DataBaseCRUD
from create_bot import bot, dispatcher
from handlers import client




async def on_startup(_):
    print("Bot stated!")

client.register_handlers_client(dispatcher)
if __name__ == '__main__':
    executor.start_polling(dispatcher, on_startup=on_startup)

