from aiogram import Bot, Dispatcher, executor, types

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


HELP_TEXT = "Any text"

async def on_startup(_):
    print("Бот успешно запущен!")

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('<em>Просто введи табельный!</em>', parse_mode='HTML')

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_TEXT)


@dp.message_handler()
async def echo(message: types.Message):
    print(message)
    await message.answer(text=message.text)



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)