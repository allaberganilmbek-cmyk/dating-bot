import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Вставьте сюда ТОЧНЫЙ токен от @BotFather
BOT_TOKEN = "8710117910:AAEbmqNdhzwfBUbHWk5tOY2nYMDLEqTb1SA"
VERCEL_WEBAPP_URL = "https://data-sandy-iota-46.vercel.app/"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔥 Запустить Знакомства",
                    web_app=WebAppInfo(url=VERCEL_WEBAPP_URL)
                )
            ]
        ]
    )

    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n\n"
        f"Добро пожаловать в приложение знакомств.\n"
        f"Нажмите на кнопку ниже, чтобы открыть анкеты:",
        reply_markup=keyboard
    )


async def main():
    print("Бот успешно запущен и работает!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())