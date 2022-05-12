# pip install aiogram
import sys
import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, \
    InlineKeyboardButton, InlineKeyboardMarkup
#   CallbackQuery, KeyboardButton

from config import TOKEN_KEY


sys.path.append('../../')

logging.basicConfig(level=logging.INFO)

TOKEN = TOKEN_KEY
print(TOKEN)
bot = Bot(TOKEN)
dp = Dispatcher(bot)


# photo = 'images/start_zastavka.png'

# __import__('section_sec')


# Пишем команду с приветствием и заставкой
@dp.message_handler(commands=['start'])
async def callback_start(message: Message):
    # await bot.send_photo(chat_id=message.chat.id, photo=
    #   'images/start_zastavka.png')
    # await bot.send_photo(chat_id=message.chat.id, types.InputFile(
    #   'images/start_zastavka.png'))
    await bot.send_message(
        chat_id=message.chat.id,
        reply_markup=choose_lang,
        text="Привет, я справочный чат-бот. Помогу вам. Выберите язык:")


# Пишем команду с приветствием и заставкой
@dp.message_handler(commands=['language'])
async def callback_language(message: Message):
    await bot.send_message(
        chat_id=message.chat.id,
        reply_markup=choose_lang,
        text="Выберите язык:")

# Создаем первую клавиатуру c выбором языка
choose_lang = InlineKeyboardMarkup().row(
    InlineKeyboardButton(text="Українськa", callback_data="get-UKR"),
    InlineKeyboardButton(text="Русский", callback_data="get-RUS"))


# Указываем, что сделать при нажатии на кнопку после выбора языка:
@dp.callback_query_handler(lambda c: c.data == 'get-UKR')
async def get_UKR(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=chosen_ukr,
        text="Виберіть країну:")


@dp.callback_query_handler(lambda c: c.data == 'get-RUS')
async def get_RUS(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        reply_markup=chosen_rus,
        text="Выберите страну:")


