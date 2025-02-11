import json
import os
from typing import Any

from src.external_api import api_convert_currency


def get_operations_from_file(path: str) -> Any:
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает список
    словарей с данными о финансовых транзакциях. Если файл пустой,
    содержит не список или не найден, функция возвращает пустой список.
    """
    if not os.path.isfile(path) or os.path.getsize(path) == 0:
        return []
    try:
        with open(path, encoding="utf-8") as file_json:
            data_from_file = json.load(file_json)
        if not isinstance(data_from_file, list):
            return []
        else:
            return data_from_file
    except json.JSONDecodeError:
        return []


def get_amount_transactions(transactions: list) -> float:
    """
    Функция, которая принимает на вход транзакцию и возвращает сумму транзакции
    (amount) в рублях, тип данных — float.
    """
    amount = 0.0
    for i in transactions:
        try:
            currency_code = i["operationAmount"]["currency"]["code"]
            amount_transaction = i["operationAmount"]["amount"]
        except KeyError:
            continue

        if not amount_transaction or not isinstance(amount_transaction, str):
            continue

        if currency_code == "RUB":
            try:
                amount += float(amount_transaction)
            except ValueError:
                continue
        elif currency_code in ["EUR", "USD"]:
            amount += api_convert_currency(currency_code, amount_transaction)
    return amount
