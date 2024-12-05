# Импорт модулей
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

# Ввод данных для маскировки и вывод результата
while True:
    user_input = input("Введите тип и номер карты или счет с номером: ")
    output_mask = mask_account_card(user_input)
    if "Ошибка" in output_mask:
        print("Введены некорректные данные, попробуйте еще раз!")
        continue
    else:
        break

print(output_mask)

# Проверка функции get_data()
print(get_date("2024-03-11T02:26:18.671407"))

# Проверка функции filter_by_state()
print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)

# Проверка функции sort_by_date()
print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        False,
    )
)
