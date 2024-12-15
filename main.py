# Импорт модулей
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

# Ввод данных пользователя, работа функции mask_account_card()
while True:
    try:
        user_input = input("Введите тип и номер карты или счет с номером: ")
        output_mask = mask_account_card(user_input)
        print(output_mask)
    except ValueError:
        print("Введены некорректные данные")
        continue
    except IndexError:
        print("Введены некорректные данные")
        continue
    else:
        break


# Работа функции get_data()
print(get_date("2024-03-11T02:26:18.671407"))

# Работа функции фильтрации данных filter_by_state() по ключу "state" значение по умолчанию "EXECUTED"
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

# Работа функции фильтрации данных filter_by_state() по ключу "state" значение "CANCELED"
print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        "CANCELED"
    )
)

# Работа функции сортировки данных sort_by_date() по ключу "date", сортировка по возрастанию
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

# Работа функции сортировки данных sort_by_date() по ключу "date", сортировка по убыванию
print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
    )
)