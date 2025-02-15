# Импорт модулей
from src.processing import filter_by_state, sort_by_date, user_input_search
from src.transactions_from_file import get_transaction_from_csv, get_transaction_from_xlsx
from src.utils import get_operations_from_file
from src.widget import get_date, mask_account_card


def print_greeting() -> None:
    """
    Функция вывода меню выбора действия
    """
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")


def main() -> None:
    """
    Функция работы программы по работе с банковскими транзакциями
    """
    flag = False
    transactions = []
    # Меню выбора действия
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    while True:
        print_greeting()
        user_input = input("Пользователь: ")
        if user_input == "1":
            transactions = get_operations_from_file("data/operations.json")
            flag = True
            break
        elif user_input == "2":
            transactions = get_transaction_from_csv("data/transactions.csv")
            break
        elif user_input == "3":
            transactions = get_transaction_from_xlsx("data/transactions_excel.xlsx")
            break
        else:
            print("Пункт меню не выбран.")
            continue

    if len(transactions) == 0:
        print("Не найдено ни одной транзакции")
        return None
    else:
        print(f"Количество транзакций {len(transactions)}.")
    # Выбор параметра фильтрации данных по ключу "state"
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        user_input = input("Пользователь: ").upper()
        if user_input in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions = filter_by_state(transactions, user_input)
            print(f'Транзакции отфильтрованы по статусу "{user_input}"')
            print(f"Количество транзакций {len(transactions)}.")
            break
        else:
            print(f'Статус операции "{user_input}" недоступен.')
            continue
    # Выбор параметра сортировки по дате
    while True:
        print("Отсортировать транзакции по дате? Да/Нет")
        user_input = input("Пользователь: ").lower()
        if user_input in ["да", "нет"]:
            if user_input == "да":
                while True:
                    print("Отсортировать по возрастанию или по убыванию?")
                    user_input = input("Пользователь: ").lower()
                    if user_input in ["по возрастанию", "по убыванию"]:
                        if user_input == "по возрастанию":
                            transactions = sort_by_date(transactions, sorted_param=False)
                            break
                        else:
                            transactions = sort_by_date(transactions)
                            break
                    else:
                        print('Введите "по возрастанию" или "по убыванию"')
                        continue
                break
            else:
                break
        else:
            print('Введите "Да" или "Нет"')
            continue

    if len(transactions) == 0:
        print("Не найдено ни одной транзакции")
        return None
    # Выбор вывода валюты транзакций (все или только в рублях)
    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        user_input = input("Пользователь: ").lower()
        if user_input in ["да", "нет"]:
            if user_input == "да":
                if flag:
                    transactions = [
                        transaction
                        for transaction in transactions
                        if transaction["operationAmount"]["currency"]["code"] == "RUB"
                    ]
                    if len(transactions) == 0:
                        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                        return None
                    break
                else:
                    transactions = [
                        transaction for transaction in transactions if transaction["currency_code"] == "RUB"
                    ]
                    break
            else:
                if len(transactions) == 0:
                    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                    return None
                break
        else:
            print('Введите "Да" или "Нет"')
            continue
    # Фильтрация транзакций по ключевому слову
    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        user_input = input("Пользователь: ").lower()
        if user_input in ["да", "нет"]:
            if user_input == "да":
                user_input = input("Введите ключевую фразу для фильтрации: ")
                transactions = user_input_search(transactions, user_input)
                break
            else:
                break
        else:
            print('Введите "Да" или "Нет"')
            continue

    if len(transactions) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return None
    # Вывод результата выборки на экран
    print("Распечатываю итоговый список транзакций...\n\n")
    print(f"Всего банковских транзакций в выборке: {len(transactions)}\n")

    for transaction in transactions:
        if "from" not in transaction.keys():
            print(f"{get_date(transaction["date"])} {transaction["description"]}")
            print(mask_account_card(transaction["to"]))
            print(
                f"Сумма: {transaction["operationAmount"]["amount"]} "
                f"{transaction["operationAmount"]["currency"]["name"]}\n"
            )
        elif not isinstance(transaction["from"], str):
            print(f"{get_date(transaction["date"])} {transaction["description"]}")
            print(mask_account_card(transaction["to"]))
            print(f"Сумма: {transaction["amount"]} {transaction["currency_name"]}\n")
        elif "operationAmount" in transaction.keys():
            print(f"{get_date(transaction["date"])} {transaction["description"]}")
            print(f"{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}")
            print(
                f"Сумма: {transaction["operationAmount"]["amount"]} "
                f"{transaction["operationAmount"]["currency"]["name"]}\n"
            )
        else:
            print(f"{get_date(transaction["date"])} {transaction["description"]}")
            print(f"{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}")
            print(f"Сумма: {transaction["amount"]} {transaction["currency_name"]}\n")

    return None


if __name__ == "__main__":
    main()
