import sqlite3

import pandas


query_for_excel_file = '''
SELECT model, version, count(version) as cnt
FROM robots_robot
WHERE created >= datetime("now", "-7 day")
GROUP by model, version
ORDER BY cnt
'''


def make_excel_file():
    conn = sqlite3.connect('db.sqlite3')

    df = pandas.read_sql(query_for_excel_file,
                         conn)

    models = df['model'].drop_duplicates()

    with pandas.ExcelWriter('excel_file.xlsx') as writer:
        for model in models:
            excel_list = df[df['model'] == model]

            excel_list.to_excel(writer,
                                sheet_name=f'model {model}',
                                index=False,
                                header=['Модель', 'Версия', 'Количество за неделю'])