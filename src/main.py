import sys
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.fsm.context import FSMContext
import markup
import states
from aiogram.filters import CommandStart
from settings import TOKEN
from db_helper import set_user_testing_results, \
                      get_user_testing_results, \
                      get_subject_choice, \
                      set_subject_choice, \
                      find_matching_specialties
import test_questions
from functools import reduce


router = Router()


@router.message(CommandStart())  # Отвечает на команду /start
async def start_command(message: types.Message, state: FSMContext) -> None:
    await message.answer(f'Для начала пройди тест, выбери предметы по которым ты сдал ЕГЭ и посмотри результат)', reply_markup=markup.markup_main())


@router.message(F.text == "Пройти тест 📃")  # Отвечает на сообщение Пройти тест и запускает машину состояний
async def process_test(message: types.Message, state: FSMContext) -> None:
    await state.set_state(states.Test.Q1)
    await message.answer(f'{test_questions.q}', reply_markup=markup.markup_main())
    await message.answer(f'{test_questions.q1a}\nИЛИ\n{test_questions.q1b}', reply_markup=markup.markup_test())


@router.message(states.Test.Q1)
async def process_test_1(message: types.Message, state: FSMContext) -> None:
    if message.text == "Первое":
        await state.update_data(S1="1a")
        await state.set_state(states.Test.Q2)
        await message.answer(f'{test_questions.q2a}\nИЛИ\n{test_questions.q2b}', reply_markup=markup.markup_test())
    elif message.text == "Второе":
        await state.update_data(S1="1b")
        await state.set_state(states.Test.Q2)
        await message.answer(f'{test_questions.q2a}\nИЛИ\n{test_questions.q2b}', reply_markup=markup.markup_test())
    else:
        await message.answer("Выбери один из предложенных вариантов.")


@router.message(states.Test.Q2)
async def process_test_2(message: types.Message, state: FSMContext) -> None:
    if message.text == "Первое":
        await state.update_data(S2="2а")
        await state.set_state(states.Test.Q3)
        await message.answer(f'{test_questions.q3a}\nИЛИ\n{test_questions.q3b}', reply_markup=markup.markup_test())
    elif message.text == "Второе":
        await state.update_data(S2="2б")
        await state.set_state(states.Test.Q3)
        await message.answer(f'{test_questions.q3a}\nИЛИ\n{test_questions.q3b}', reply_markup=markup.markup_test())
    else:
        await message.answer("Выбери один из предложенных вариантов.")


@router.message(states.Test.Q3)
async def process_test_3(message: types.Message, state: FSMContext) -> None:
    if message.text == "Первое":
        await state.update_data(S3="3а")
        await state.set_state(states.Test.Q4)
        await message.answer(f'{test_questions.q4a}\nИЛИ\n{test_questions.q4b}', reply_markup=markup.markup_test())
    elif message.text == "Второе":
        await state.update_data(S3="3б")
        await state.set_state(states.Test.Q4)
        await message.answer(f'{test_questions.q4a}\nИЛИ\n{test_questions.q4b}', reply_markup=markup.markup_test())
    else:
        await message.answer("Выбери один из предложенных вариантов.")

@router.message(states.Test.Q4)
async def process_test_4(message: types.Message, state: FSMContext) -> None:
    if message.text == "Первое":
        await state.update_data(S4="4а")
        await state.set_state(states.Test.Q5)
        await message.answer(f'{test_questions.q5a}\nИЛИ\n{test_questions.q5b}', reply_markup=markup.markup_test())
    elif message.text == "Второе":
        await state.update_data(S4="4б")
        await state.set_state(states.Test.Q5)
        await message.answer(f'{test_questions.q5a}\nИЛИ\n{test_questions.q5b}', reply_markup=markup.markup_test())
    else:
        await message.answer("Выбери один из предложенных вариантов.")

@router.message(states.Test.Q5)
async def process_test_5(message: types.Message, state: FSMContext) -> None:
    if message.text == "Первое":
        await state.update_data(S5="5а")
        await state.set_state(states.Test.Q6)
        await message.answer(f'{test_questions.q6a}\nИЛИ\n{test_questions.q6b}', reply_markup=markup.markup_test())
    elif message.text == "Второе":
        await state.update_data(S5="5б")
        await state.set_state(states.Test.Q6)
        await message.answer(f'{test_questions.q6a}\nИЛИ\n{test_questions.q6b}', reply_markup=markup.markup_test())
    else:
        await message.answer("Выбери один из предложенных вариантов.")





@router.message(states.Test.Q6)
async def process_test_6(message: types.Message, state: FSMContext) -> None:
    if message.text == "Первое":
        await state.update_data(S6="6а")
        await state.set_state(states.Test.Q7)
        await message.answer(f'{test_questions.q7a}\nИЛИ\n{test_questions.q7b}', reply_markup=markup.markup_test())
    elif message.text == "Второе":
        await state.update_data(S6="6б")
        await state.set_state(states.Test.Q7)
        await message.answer(f'{test_questions.q7a}\nИЛИ\n{test_questions.q7b}', reply_markup=markup.markup_test())
    else:
        await message.answer("Выбери один из предложенных вариантов.")

@router.message(states.Test.Q7)
async def process_test_7(message: types.Message, state: FSMContext) -> None:
    if message.text == "Первое":
        await state.update_data(S7="7а")
        await state.set_state(states.Test.Q8)
        await message.answer(f'{test_questions.q8a}\nИЛИ\n{test_questions.q8b}', reply_markup=markup.markup_test())
    elif message.text == "Второе":
        await state.update_data(S7="7б")
        await state.set_state(states.Test.Q8)
        await message.answer(f'{test_questions.q8a}\nИЛИ\n{test_questions.q8b}', reply_markup=markup.markup_test())
    else:
        await message.answer("Выбери один из предложенных вариантов.")

@router.message(states.Test.Q8)
async def process_test_8(message: types.Message, state: FSMContext) -> None:
    if message.text == "Первое":
        await state.update_data(S8="8а")
        await state.set_state(states.Test.Q9)
        await message.answer(f'{test_questions.q9a}\nИЛИ\n{test_questions.q9b}', reply_markup=markup.markup_test())
    elif message.text == "Второе":
        await state.update_data(S8="8б")
        await state.set_state(states.Test.Q9)
        await message.answer(f'{test_questions.q9a}\nИЛИ\n{test_questions.q9b}', reply_markup=markup.markup_test())
    else:
        await message.answer("Выбери один из предложенных вариантов.")



@router.message(states.Test.Q9)
async def process_test_9(message: types.Message, state: FSMContext) -> None:
    if message.text == "Первое":
        await state.update_data(S9="9а")
        await state.set_state(states.Test.Q10)
        await message.answer(f'{test_questions.q10a}\nИЛИ\n{test_questions.q10b}', reply_markup=markup.markup_test())
    elif message.text == "Второе":
        await state.update_data(S9="9б")
        await state.set_state(states.Test.Q10)
        await message.answer(f'{test_questions.q10a}\nИЛИ\n{test_questions.q10b}', reply_markup=markup.markup_test())
    else:
        await message.answer("Выбери один из предложенных вариантов.")

@router.message(states.Test.Q10)
async def process_test_10(message: types.Message, state: FSMContext) -> None:
    if message.text == "Первое":
        await state.update_data(S10="10а")
        await state.set_state(states.Test.Q11)
        await message.answer(f'{test_questions.q11a}\nИЛИ\n{test_questions.q11b}', reply_markup=markup.markup_test())
    elif message.text == "Второе":
        await state.update_data(S10="10б")
        await state.set_state(states.Test.Q11)
        await message.answer(f'{test_questions.q11a}\nИЛИ\n{test_questions.q11b}', reply_markup=markup.markup_test())
    else:
        await message.answer("Выбери один из предложенных вариантов.")

@router.message(states.Test.Q11)
async def process_test_11(message: types.Message, state: FSMContext) -> None:
    if message.text == "Первое":
        await state.update_data(S11="11а")
        await state.set_state(states.Test.Q12)
        await message.answer(f'{test_questions.q12a}\nИЛИ\n{test_questions.q12b}', reply_markup=markup.markup_test())
    elif message.text == "Второе":
        await state.update_data(S11="11б")
        await state.set_state(states.Test.Q12)
        await message.answer(f'{test_questions.q12a}\nИЛИ\n{test_questions.q12b}', reply_markup=markup.markup_test())
    else:
        await message.answer("Выбери один из предложенных вариантов.")




@router.message(states.Test.Q12)
async def process_test_12(message: types.Message, state: FSMContext) -> None:
    if message.text == "Первое":
        await state.update_data(S12="12а")
        await state.set_state(states.Test.Q13)
        await message.answer(f'{test_questions.q13a}\nИЛИ\n{test_questions.q13b}', reply_markup=markup.markup_test())
    elif message.text == "Второе":
        await state.update_data(S12="12б")
        await state.set_state(states.Test.Q13)
        await message.answer(f'{test_questions.q13a}\nИЛИ\n{test_questions.q13b}', reply_markup=markup.markup_test())
    else:
        await message.answer("Выбери один из предложенных вариантов.")

@router.message(states.Test.Q13)
async def process_test_13(message: types.Message, state: FSMContext) -> None:
    if message.text == "Первое":
        await state.update_data(S13="13а")
        await state.set_state(states.Test.Q14)
        await message.answer(f'{test_questions.q14a}\nИЛИ\n{test_questions.q14b}', reply_markup=markup.markup_test())
    elif message.text == "Второе":
        await state.update_data(S13="13б")
        await state.set_state(states.Test.Q14)
        await message.answer(f'{test_questions.q14a}\nИЛИ\n{test_questions.q14b}', reply_markup=markup.markup_test())
    else:
        await message.answer("Выбери один из предложенных вариантов.")

@router.message(states.Test.Q14)
async def process_test_14(message: types.Message, state: FSMContext) -> None:
    if message.text == "Первое":
        await state.update_data(S14="14а")
        await state.set_state(states.Test.Q15)
        await message.answer(f'{test_questions.q15a}\nИЛИ\n{test_questions.q15b}', reply_markup=markup.markup_test())
    elif message.text == "Второе":
        await state.update_data(S14="14б")
        await state.set_state(states.Test.Q15)
        await message.answer(f'{test_questions.q15a}\nИЛИ\n{test_questions.q15b}', reply_markup=markup.markup_test())
    else:
        await message.answer("Выбери один из предложенных вариантов.")

@router.message(states.Test.Q15)
async def process_test_15(message: types.Message, state: FSMContext) -> None:
    if message.text == "Первое":
        await state.update_data(S15="15а")
        await state.set_state(states.Test.Q16)
        await message.answer(f'{test_questions.q16a}\nИЛИ\n{test_questions.q16b}', reply_markup=markup.markup_test())
    elif message.text == "Второе":
        await state.update_data(S15="15б")
        await state.set_state(states.Test.Q16)
        await message.answer(f'{test_questions.q16a}\nИЛИ\n{test_questions.q16b}', reply_markup=markup.markup_test())
    else:
        await message.answer("Выбери один из предложенных вариантов.")




@router.message(states.Test.Q16)
async def process_test_16(message: types.Message, state: FSMContext) -> None:
    if message.text == "Первое":
        await state.update_data(S16="16а")
        await state.set_state(states.Test.Q17)
        await message.answer(f'{test_questions.q17a}\nИЛИ\n{test_questions.q17b}', reply_markup=markup.markup_test())
    elif message.text == "Второе":
        await state.update_data(S16="16б")
        await state.set_state(states.Test.Q17)
        await message.answer(f'{test_questions.q17a}\nИЛИ\n{test_questions.q17b}', reply_markup=markup.markup_test())
    else:
        await message.answer("Выбери один из предложенных вариантов.")


@router.message(states.Test.Q17)
async def process_test_17(message: types.Message, state: FSMContext) -> None:
    if message.text == "Первое":
        await state.update_data(S17="17а")
        await state.set_state(states.Test.Q18)
        await message.answer(f'{test_questions.q18a}\nИЛИ\n{test_questions.q18b}', reply_markup=markup.markup_test())
    elif message.text == "Второе":
        await state.update_data(S17="17б")
        await state.set_state(states.Test.Q18)
        await message.answer(f'{test_questions.q18a}\nИЛИ\n{test_questions.q18b}', reply_markup=markup.markup_test())
    else:
        await message.answer("Выбери один из предложенных вариантов.")


@router.message(states.Test.Q18)
async def process_test_18(message: types.Message, state: FSMContext) -> None:
    if message.text == "Первое":
        await state.update_data(S18="18а")
        await state.set_state(states.Test.Q19)
        await message.answer(f'{test_questions.q19a}\nИЛИ\n{test_questions.q19b}', reply_markup=markup.markup_test())
    elif message.text == "Второе":
        await state.update_data(S18="18б")
        await state.set_state(states.Test.Q19)
        await message.answer(f'{test_questions.q19a}\nИЛИ\n{test_questions.q19b}', reply_markup=markup.markup_test())
    else:
        await message.answer("Выбери один из предложенных вариантов.")


@router.message(states.Test.Q19)
async def process_test_19(message: types.Message, state: FSMContext) -> None:
    if message.text == "Первое":
        await state.update_data(S19="19а")
        await state.set_state(states.Test.Q20)
        await message.answer(f'{test_questions.q20a}\nИЛИ\n{test_questions.q20b}', reply_markup=markup.markup_test())
    elif message.text == "Второе":
        await state.update_data(S19="19б")
        await state.set_state(states.Test.Q20)
        await message.answer(f'{test_questions.q20a}\nИЛИ\n{test_questions.q20b}', reply_markup=markup.markup_test())
    else:
        await message.answer("Выбери один из предложенных вариантов.")


@router.message(states.Test.Q20)
async def process_test_20(message: types.Message, state: FSMContext) -> None:
    if message.text == "Первое":
        await state.update_data(S19="20а")
    elif message.text == "Второе":
        await state.update_data(S19="20б")
    else:
        await message.answer("Выбери один из предложенных вариантов.")
        return 
        
    data = await state.get_data()

    psycho_types = [(1, ['1а','3б', '6а', '10а', '11а', '13б', '16а', '20а']),
                    (2, ['1б','4а', '7б', '9а', '11б', '14а', '19а']),
                    (3, ['2a','4б', '6б', '8а', '12а', '14б']),
                    (4, ['2б','5а', '9б', '10б', '12б', '15а', '19б', '20б'])]

    ans = []
    for i in data.keys():
        ans.append(data[i])

    max = 0
    max_type = 0
    for i in range(len(psycho_types)):
        if reduce(lambda x, y: x+psycho_types[i][1].count(y), set(ans), 0) > max:
            max = reduce(lambda x, y: x+psycho_types[i][1].count(y), set(ans), 0)
            max_type = i+1

    if max_type == 1:
        data_testing = 'Человек - природа'
    if max_type == 2:
        data_testing = 'Человек - техника'
    if max_type == 3:
        data_testing = 'Человек - человек'
    if max_type == 4:
        data_testing = 'Человек - знаковая техника, знаковый образ'

    await set_user_testing_results(message.from_user.id, max_type)
    await state.clear()
    await message.answer(f'Опрос завершён {data_testing}', reply_markup=markup.markup_main())


@router.message(F.text == "Посмотреть результат 🖨️")  # Отвечает на сообщение Пройти тест и запускает машину состояний
async def process_test(message: types.Message) -> None:
    result = await get_user_testing_results(message.from_user.id)
    data_subjects = await get_subject_choice(message.from_user.id)

    if result:
        if result == 1:
            data_testing = 'Человек - природа'
        if result == 2:
            data_testing = 'Человек - техника'
        if result == 3:
            data_testing = 'Человек - человек'
        if result == 4:
            data_testing = 'Человек - знаковая техника, знаковый образ'


    if result and data_testing and data_subjects:
        await message.answer(f'{data_testing}', reply_markup=markup.markup_main())
        subjects = [f"{i['subject']}: {i['score']} баллов" for i in data_subjects['Choose']]
        await message.answer('\n'.join(subjects), reply_markup=markup.markup_main())
        user_subject = await get_subject_choice(user_id=message.from_user.id)
        specialties = await find_matching_specialties(sum([i['score'] for i in data_subjects['Choose']]), result, user_subject)
        if specialties:
            for specialty in specialties:
                await message.answer(f'{specialty}', reply_markup=markup.markup_main())
        else:
            await message.answer(f'Специальности под ваши баллы не найдены', reply_markup=markup.markup_main())


    elif result and data_testing:
        await message.answer(f'{data_testing}', reply_markup=markup.markup_main())
        await message.answer(f'Введить предметы которые сдавали', reply_markup=markup.markup_main())
    elif data_subjects:
        subjects = [f"{i['subject']}: {i['score']} баллов" for i in data_subjects['Choose']]
        await message.answer('\n'.join(subjects), reply_markup=markup.markup_main())
        await message.answer(f'Пройдите профтест', reply_markup=markup.markup_main())
    else:
        await message.answer("У вас нет результатов тестирования!", reply_markup=markup.markup_main())


@router.message(F.text == "Выбрать предметы 📖")
async def choose_subjects(message: types.Message, state: FSMContext):
    await state.set_state(states.Subjects.Choose)
    await message.answer("Выбери предметы, по которым ты сдавал экзамены и укажите баллы.\n"
                         "Для выбора нескольких предметов используйте кнопки выбора.\n"
                         "Для завершения выбора нажмите кнопку 'Готово'.",
                         reply_markup=markup.markup_subjects())


@router.message(states.Subjects.Choose, F.text == "Готово")
async def process_exam_scores(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await state.clear()    
    if 'Choose' not in data:
        await message.answer(f"Вы ничего не изменили", reply_markup=markup.markup_main())
        return


    data_subjects = await get_subject_choice(user_id=message.from_user.id)
    if data_subjects and ('Choose' in data_subjects):
        i = 0
        for sub in data['Choose']:
            if sub['subject'] in [subject['subject'] for subject in data_subjects['Choose']]:
                data_subjects['Choose'].pop(i)
            data_subjects['Choose'].append(sub)
            i += 1
        await set_subject_choice(user_id=message.from_user.id, subjects=data_subjects)
        data = [f"{i['subject']}: {i['score']} баллов" for i in data['Choose']]
    else:
        data = [f"{i['subject']}: {i['score']} баллов" for i in data['Choose']]
        await set_subject_choice(user_id=message.from_user.id, subjects=data)


    await message.answer(f'Выбранные предметы и баллы по экзаменам:\n{" ".join(data)}', reply_markup=markup.markup_main())




@router.message(states.Subjects.Choose)
async def process_subject_choice(message: types.Message, state: FSMContext):
    data = await state.get_data()
    
    if 'Choose' not in data:
        data['Choose'] = []

    if message.text in [button.text for row in markup.markup_subjects().keyboard for button in row]:
        if any(subject['subject'] == message.text for subject in data['Choose']):
            data['Choose'].pop([subject['subject'] for subject in data['Choose']].index(message.text))

        data['Choose'].append({'subject': message.text, 'score': None})
        await state.update_data(data)
        await message.answer(f"Выбран предмет: {message.text}. Укажите баллы по этому предмету.")
    else:
        try:
            score = int(message.text)
        except ValueError:
            await message.answer("Пожалуйста, введите число.")
            return

        if not 0 <= score <= 100:
            await message.answer("Пожалуйста, введите число от 0 до 100.")
            return

        data = await state.get_data()
        last_subject = data['Choose'][-1]
        last_subject_index = len(data['Choose']) - 1

        data['Choose'][last_subject_index]['score'] = score

        await state.update_data(data)

        await message.answer(f"Баллы по предмету '{last_subject['subject']}' успешно учтены. "
                             f"Выберите следующий предмет или нажмите 'Готово', чтобы завершить выбор.",
                             reply_markup=markup.markup_subjects() if last_subject_index < len(markup.markup_subjects().keyboard) else None)


@router.message()
async def process_test(message: types.Message) -> None:
    await message.answer(f'Я не понимаю вашего запроса', reply_markup=markup.markup_main())


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logging.getLogger('matplotlib.font_manager').disabled = True
    asyncio.run(main())
