from aiogram import Bot, Dispatcher, executor, types
import os

TOKEN = os.environ['TOKEN_TG']

bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)
