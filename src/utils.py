import json
import os
from decimal import Decimal
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
    with open(path, encoding="utf-8") as file_json:
        data_from_file = json.load(file_json)
    if not isinstance(data_from_file, list):
        return []
    else:
        return data_from_file


def get_amount_transactions(transactions: list) -> float:
    """
    Функция, которая принимает на вход транзакцию и возвращает сумму транзакции
    (amount) в рублях, тип данных — float. Если транзакция была в USD или EUR,
    происходит обращение к внешнему API для получения текущего курса валют и
    конвертации суммы операции в рубли.
    Для конвертации валюты используется Exchange Rates Data API
    """
    amount = 0

    for i in transactions:
        currency_code = i.get("operationAmount", {}).get("currency", {}).get("code", None)
        amount_transaction = i.get("operationAmount", {}).get("amount", None)
        if currency_code == "RUB":
            amount += float(Decimal(amount_transaction))
        elif currency_code == "EUR" or currency_code == "USD":
            amount += api_convert_currency(currency_code, amount_transaction)
    return amount
