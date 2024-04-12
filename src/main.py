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


@router.message(CommandStart())  # Отвечает на команду /start
async def start_command(message: types.Message, state: FSMContext) -> None:
    await message.answer(f'Добрый день пользователе! Я помогу тебе определитиься с выбором направления в которое тебе пойти)', reply_markup=src.markup.markup_main())


@router.message(F.text == "Пройти тест")  # Отвечает на сообщение Пройти тест и запускает машину состояний
async def process_test(message: types.Message, state: FSMContext) -> None:
    await state.set_state(src.states.Test.Q1)
    await message.answer(f'Вопрос 1', reply_markup=src.markup.markup_test_1())


@router.message(src.states.Test.Q1)
async def process_test_1(message: types.Message, state: FSMContext) -> None:
    await state.update_data(S1=message.text)
    await state.set_state(src.states.Test.Q2)
    await message.answer(f'Вопрос 2', reply_markup=src.markup.markup_test_2())


@router.message(src.states.Test.Q2)
async def process_test_2(message: types.Message, state: FSMContext) -> None:
    await state.update_data(S2=message.text)
    await state.set_state(src.states.Test.Q3)
    await message.answer(f'Вопрос 3', reply_markup=src.markup.markup_test_3())


@router.message(src.states.Test.Q3)
async def process_test_3(message: types.Message, state: FSMContext) -> None:
    await state.update_data(S3=message.text)
    await state.set_state(src.states.Test.Q4)
    await message.answer(f'Вопрос 4', reply_markup=src.markup.markup_test_4())


@router.message(src.states.Test.Q4)
async def process_test_4(message: types.Message, state: FSMContext) -> None:
    await state.update_data(S4=message.text)
    await state.set_state(src.states.Test.Q5)
    await message.answer(f'Вопрос 5', reply_markup=src.markup.markup_test_5())


@router.message(src.states.Test.Q5)
async def process_test_5(message: types.Message, state: FSMContext) -> None:
    await state.update_data(S5=message.text)
    await state.set_state(src.states.Test.Q6)
    await message.answer(f'Вопрос 6', reply_markup=src.markup.markup_test_6())


@router.message(src.states.Test.Q6)
async def process_test_6(message: types.Message, state: FSMContext) -> None:
    await state.update_data(S6=message.text)
    await state.set_state(src.states.Test.Q7)
    await message.answer(f'Вопрос 7', reply_markup=src.markup.markup_test_7())


@router.message(src.states.Test.Q7)
async def process_test_7(message: types.Message, state: FSMContext) -> None:
    await state.update_data(S7=message.text)
    await state.set_state(src.states.Test.Q8)
    await message.answer(f'Вопрос 8', reply_markup=src.markup.markup_test_8())


@router.message(src.states.Test.Q8)
async def process_test_8(message: types.Message, state: FSMContext) -> None:
    await state.update_data(S8=message.text)
    await state.set_state(src.states.Test.Q9)
    await message.answer(f'Вопрос 9', reply_markup=src.markup.markup_test_9())


@router.message(src.states.Test.Q9)
async def process_test_9(message: types.Message, state: FSMContext) -> None:
    await state.update_data(S9=message.text)
    await state.set_state(src.states.Test.Q10)
    await message.answer(f'Вопрос 10', reply_markup=src.markup.markup_test_10())


@router.message(src.states.Test.Q10)
async def process_test_10(message: types.Message, state: FSMContext) -> None:
    await state.update_data(S10=message.text)
    await state.set_state(src.states.Test.Q11)
    await message.answer(f'Вопрос 11', reply_markup=src.markup.markup_test_11())


@router.message(src.states.Test.Q11)
async def process_test_11(message: types.Message, state: FSMContext) -> None:
    await state.update_data(S11=message.text)
    await state.set_state(src.states.Test.Q12)
    await message.answer(f'Вопрос 12', reply_markup=src.markup.markup_test_12())


@router.message(src.states.Test.Q12)
async def process_test_12(message: types.Message, state: FSMContext) -> None:
    await state.update_data(S12=message.text)
    await state.set_state(src.states.Test.Q13)
    await message.answer(f'Вопрос 13', reply_markup=src.markup.markup_test_13())


@router.message(src.states.Test.Q13)
async def process_test_12(message: types.Message, state: FSMContext) -> None:
    await state.update_data(S13=message.text)
    await state.set_state(src.states.Test.Q14)
    await message.answer(f'Вопрос 14', reply_markup=src.markup.markup_test_14())


@router.message(src.states.Test.Q14)
async def process_test_13(message: types.Message, state: FSMContext) -> None:
    await state.update_data(S14=message.text)
    await state.set_state(src.states.Test.Q15)
    await message.answer(f'Вопрос 15', reply_markup=src.markup.markup_test_15())


@router.message(src.states.Test.Q15)
async def process_test_14(message: types.Message, state: FSMContext) -> None:
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
