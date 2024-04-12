import asyncio
import aiogram
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Command
# from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle, CallbackQuery
from aiogram.dispatcher.filters.state import State, StatesGroup
import lib.markup


logging.basicConfig(level=logging.DEBUG)
logging.getLogger('matplotlib.font_manager').disabled = True

bot = Bot(token='7037158023:AAHsMmQDnjx_p5c1rb4E4HIQogINIXbNXwM')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'], state="*")
async def start_command(message: types.Message):
    await message.reply(f'User id {message.from_user.id} add in database.', reply_markup=lib.markup.markup_main())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.create_task(send_time())
    try:
        aiogram.executor.start_polling(dp, skip_updates=True, loop=loop)
    finally:
        loop.close()
