import json
import asyncio
import aiosqlite
import csv
import sqlite3

async def create_table():
    async with aiosqlite.connect("src/mydatabase.db") as con:
        cur = await con.cursor()
        await cur.execute("CREATE TABLE IF NOT EXISTS test_results (user_id INTEGER PRIMARY KEY, results INT, subjects TEXT)")
        await con.commit()


async def create_specialties_table():
    async with aiosqlite.connect("src/mydatabase.db") as con:
        await con.execute('''CREATE TABLE IF NOT EXISTS specialties (specialty_id TEXT, specialty_name TEXT, min_score INTEGER, avg_score INTEGER, psycho_type INT, subjects TEXT)
                            ''')
        await con.commit()


async def set_user_testing_results(user_id: int, results: int):
    async with aiosqlite.connect("src/mydatabase.db") as con:
        subjects = await get_subject_choice(user_id=user_id)
        subjects_json = json.dumps(subjects)
        await con.execute("INSERT OR REPLACE INTO test_results (user_id, results, subjects) VALUES (?, ?, ?)", (user_id, results, subjects_json))
        await con.commit()


async def get_user_testing_results(user_id: int) -> int:
    async with aiosqlite.connect("src/mydatabase.db") as con:
        cur = await con.cursor()
        await cur.execute("SELECT results FROM test_results WHERE user_id = ?", (user_id,))
        result = await cur.fetchone()
        if result and result[0] is not None:
            return result[0]  # Возвращаем только значение результата
        else:
            return None


async def delete_user_testing_results(user_id: int):
    async with aiosqlite.connect("src/mydatabase.db") as con:
        await con.execute("DELETE FROM test_results WHERE user_id = ?", (user_id,))
        await con.commit()


async def set_subject_choice(user_id: int, subjects: dict):
    async with aiosqlite.connect("src/mydatabase.db") as con:
        subjects_json = json.dumps(subjects)
        results = await get_user_testing_results(user_id=user_id)
        print(subjects_json)
        results_json = None
        if results:
            if results is set:
                results = int(results[0])
            results_json = json.dumps(results)
        await con.execute("INSERT OR REPLACE INTO test_results (user_id, results, subjects) VALUES (?, ?, ?)", (user_id, results_json, subjects_json))
        await con.commit()


async def get_subject_choice(user_id: int) -> dict:
    async with aiosqlite.connect("src/mydatabase.db") as con:
        cur = await con.cursor()
        await cur.execute("SELECT subjects FROM test_results WHERE user_id = ?", (user_id,))
        result = await cur.fetchone()
        if result and result[0]:
            subjects_json = result[0]
            return json.loads(subjects_json)
        else:
            return None

async def find_matching_specialties(sum_score: int, psycho_type: int, subjects: dict):
    async with aiosqlite.connect("src/mydatabase.db") as con:
        cur = await con.cursor()
        # print(psycho_type, sum_score)
        await cur.execute("SELECT specialty_id, specialty_name, min_score, avg_score, subjects FROM specialties WHERE psycho_type = ? AND avg_score < ?", (psycho_type, sum_score))
        result = await cur.fetchall() 
        # print(result)

        for i in range(len(result)):
            print(result[i])

        print('stalo \n\n')

        if result and result[0] is not None:
            i = 0
            for res in result:
                res = list(res)
                res[4] = res[4].replace(',', ' ')
                res[4] = res[4].replace('/', ' ')
                res[4] = res[4].split()

                if any([r not in [subject['subject'].lower() for subject in subjects['Choose']] for r in res[4]]):
                    print(result[i])
                    result.pop(i)

            return result
        else:
            return None

async def main():
    await create_specialties_table()
    await create_table()

    conn = sqlite3.connect('src/mydatabase.db')
    cursor = conn.cursor()

    with open('src/courses.csv', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Пропускаем заголовок

        for row in csvreader:
            print(len(row), row)
            # Вставляем данные из CSV файла в таблицу
            cursor.execute('INSERT INTO specialties VALUES (?, ?, ?, ?, ?, ?)', row)

    # Сохраняем изменения и закрываем соединение с базой данных
    conn.commit()
    conn.close()

if __name__ == '__main__':
    asyncio.run(main())
