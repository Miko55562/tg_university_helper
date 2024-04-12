import sys
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.fsm.context import FSMContext
import src.markup
import src.states
from aiogram.filters import CommandStart
from settings import TOKEN

router = Router()


@router.message(CommandStart())
async def start_command(message: types.Message, state: FSMContext):
    await message.answer(f'Добрый день пользователе! Я помогу тебе определитиься с выбором направления в которое тебе пойти)', reply_markup=src.markup.markup_main())


@router.message(F.text == "Пройти тест")
async def process_test(message: types.Message, state: FSMContext):
    await state.set_state(src.states.Test.S1)
    await message.answer(f'Вопрос 1', reply_markup=src.markup.markup_main())


@router.message(src.states.Test.S1)
async def process_test_1(message: types.Message, state: FSMContext):
    await state.update_data(S1=message.text)
    await state.set_state(src.states.Test.S2)
    await message.answer(f'Вопрос 2', reply_markup=src.markup.markup_main())


@router.message(src.states.Test.S2)
async def process_test_2(message: types.Message, state: FSMContext):
    await state.update_data(S2=message.text)
    await state.set_state(src.states.Test.S3)
    await message.answer(f'Вопрос 3', reply_markup=src.markup.markup_main())


@router.message(src.states.Test.S3)
async def process_test_3(message: types.Message, state: FSMContext):
    await state.update_data(S3=message.text)
    await state.set_state(src.states.Test.S4)
    await message.answer(f'Вопрос 4', reply_markup=src.markup.markup_main())


@router.message(src.states.Test.S4)
async def process_test_4(message: types.Message, state: FSMContext):
    await state.update_data(S4=message.text)
    await state.set_state(src.states.Test.S5)
    await message.answer(f'Вопрос 5', reply_markup=src.markup.markup_main())


@router.message(src.states.Test.S5)
async def process_test_5(message: types.Message, state: FSMContext):
    await state.update_data(S5=message.text)
    await state.set_state(src.states.Test.S6)
    await message.answer(f'Вопрос 6', reply_markup=src.markup.markup_main())


@router.message(src.states.Test.S6)
async def process_test_6(message: types.Message, state: FSMContext):
    await state.update_data(S6=message.text)
    await state.set_state(src.states.Test.S7)
    await message.answer(f'Вопрос 7', reply_markup=src.markup.markup_main())


@router.message(src.states.Test.S7)
async def process_test_7(message: types.Message, state: FSMContext):
    await state.update_data(S7=message.text)
    await state.set_state(src.states.Test.S8)
    await message.answer(f'Вопрос 8', reply_markup=src.markup.markup_main())


@router.message(src.states.Test.S8)
async def start_command(message: types.Message, state: FSMContext):
    await state.update_data(S8=message.text)
    await state.set_state(src.states.Test.S9)
    await message.answer(f'Вопрос 9', reply_markup=src.markup.markup_main())


@router.message(src.states.Test.S9)
async def start_command(message: types.Message, state: FSMContext):
    await state.update_data(S9=message.text)
    await state.set_state(src.states.Test.S10)
    await message.answer(f'Вопрос 10', reply_markup=src.markup.markup_main())


@router.message(src.states.Test.S10)
async def start_command(message: types.Message, state: FSMContext):
    await state.update_data(S10=message.text)
    await state.set_state(src.states.Test.S11)
    await message.answer(f'Вопрос 11', reply_markup=src.markup.markup_main())


@router.message(src.states.Test.S11)
async def start_command(message: types.Message, state: FSMContext):
    await state.update_data(S11=message.text)
    await state.set_state(src.states.Test.S12)
    await message.answer(f'Вопрос 12', reply_markup=src.markup.markup_main())


@router.message(src.states.Test.S12)
async def start_command(message: types.Message, state: FSMContext):
    await state.update_data(S12=message.text)
    await state.set_state(src.states.Test.S13)
    await message.answer(f'Вопрос 13', reply_markup=src.markup.markup_main())


@router.message(src.states.Test.S13)
async def start_command(message: types.Message, state: FSMContext):
    await state.update_data(S13=message.text)
    await state.set_state(src.states.Test.S14)
    await message.answer(f'Вопрос 14', reply_markup=src.markup.markup_main())


@router.message(src.states.Test.S14)
async def start_command(message: types.Message, state: FSMContext):
    await state.update_data(S14=message.text)
    await state.set_state(src.states.Test.S15)
    await message.answer(f'Вопрос 15', reply_markup=src.markup.markup_main())


@router.message(src.states.Test.S15)
async def start_command(message: types.Message, state: FSMContext):
    await state.update_data(S15=message.text)
    data = await state.get_data()
    await state.clear()
    await message.answer(f'Опрос завершён {data}', reply_markup=src.markup.markup_main())


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logging.getLogger('matplotlib.font_manager').disabled = True
    asyncio.run(main())
