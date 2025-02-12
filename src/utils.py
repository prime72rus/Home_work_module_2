import json
import logging
import os
from typing import Any

from src.external_api import api_convert_currency

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/utils.log', mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_operations_from_file(path: str) -> Any:
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает список
    словарей с данными о финансовых транзакциях. Если файл пустой,
    содержит не список или не найден, функция возвращает пустой список.
    """
    if not os.path.isfile(path) or os.path.getsize(path) == 0:
        logger.warning(f"{get_operations_from_file.__name__} Файл не найден или пуст")
        return []
    try:
        logger.info(f"{get_operations_from_file.__name__} Чтение данных из файла {path}")
        with open(path, encoding="utf-8") as file_json:
            data_from_file = json.load(file_json)
        if not isinstance(data_from_file, list):
            logger.error(f"{get_operations_from_file.__name__} Ошибка: некорректные данные")
            return []
        else:
            logger.info(f"{get_operations_from_file.__name__} Данные из файла получены")
            return data_from_file
    except json.JSONDecodeError:
        logger.error(f"{get_operations_from_file.__name__} Ошибка декодирования данных")
        return []


def get_amount_transactions(transactions: list) -> float:
    """
    Функция, которая принимает на вход транзакцию и возвращает сумму транзакции
    (amount) в рублях, тип данных — float.
    """
    amount = 0.0
    for i in transactions:
        try:
            logger.info(f"{get_amount_transactions.__name__} Получение данных для подсчета суммы по операциям")
            currency_code = i["operationAmount"]["currency"]["code"]
            amount_transaction = i["operationAmount"]["amount"]
        except KeyError:
            logger.error(f"{get_amount_transactions.__name__} Ошибка: ключ не найден, транзакция пропущена")
            continue

        if not amount_transaction or not isinstance(amount_transaction, str):
            logger.error(f"{get_amount_transactions.__name__} "
                         f"Ошибка: несоответствие входных данных, транзакция пропущена")
            continue

        if currency_code == "RUB":
            try:
                logger.info(f"{get_amount_transactions.__name__} Транзакция в рублях")
                amount += float(amount_transaction)
            except ValueError:
                logger.error(f"{get_amount_transactions.__name__} Ошибка: некорректные данные")
                continue
        elif currency_code in ["EUR", "USD"]:
            logger.info(f"{get_amount_transactions.__name__} Транзакция в валюте, конвертация в рубли")
            amount += api_convert_currency(currency_code, amount_transaction)
    return amount
