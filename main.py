import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup
from aiogram.filters import CommandStart
from aiogram.types.keyboard_button import KeyboardButton

# Объект бота
bot = Bot(token="6686787815:AAHR_PCRpxHDwzvDo5aGBmaZX-JRKnKD_mc")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(CommandStart())
async def cmd_start(message: Message):
    kb = [
        [
            KeyboardButton(text='1'),
            KeyboardButton(text='2')
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder='Введите код из под видео'
        )
    await message.answer('Код?', reply_markup=keyboard)

# Хэндлер на кнопку 1
@dp.message(F.text.lower() == '1')
async def code_one(message=Message):
    await message.answer('Пе')

# Хэндлер на кнопку 2
@dp.message(F.text.lower() == '2')
async def code_one(message=Message):
    await message.answer('')

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)    # Включаем логирование, чтобы не пропустить важные сообщения
    asyncio.run(main())