from typing import Any, Generator


def filter_by_currency(transactions_list: list[dict], target_currency: str) -> Generator[dict[Any, Any]]:
    """
    Функция принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD).
    """
    for transaction in transactions_list:
        if transaction["operationAmount"]["currency"]["name"] == target_currency:
            yield transaction


def transaction_descriptions(transactions_list: list[Any]) -> Generator[str]:
    """
    Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
    """
    for transaction in transactions_list:
        yield str(transaction["description"])


def card_number_generator(start: int, stop: int) -> Generator[str]:
    """
    Функция-генератор, которая выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров.
    """
    if start > stop or start <= 0 or stop < 0 or stop > 9999_9999_9999_9999:
        raise ValueError("Ошибка ввода диапазона")
    for i in range(start, stop + 1):
        count_zero = "0" * (16 - len(str(i)))
        number_card = count_zero + str(i)
        yield f"{number_card[0:4]} {number_card[4:8]} {number_card[8:12]} {number_card[12:]}"
