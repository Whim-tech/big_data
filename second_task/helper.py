import datetime

persons_ids = [
 782898, # Шарун
 36240,  # Мунько
 709789, # Федотова
 1076,   # Прохоров
]

for id in persons_ids:

    start_date = "2023.08.28"
    date = datetime.datetime.strptime(start_date, "%Y.%m.%d")

    while(date < datetime.datetime.fromisoformat('2024-01-01')):
        start_date = date
        start_date_str = start_date.strftime("%Y.%m.%d")

        end_date = date + datetime.timedelta(days=6)
        end_date_str = end_date.strftime("%Y.%m.%d")

        print(f"https://rasp.omgtu.ru/api/schedule/person/{id}?start={start_date_str}&finish={end_date_str}&lng=1")

        date = date + datetime.timedelta(days=7)
