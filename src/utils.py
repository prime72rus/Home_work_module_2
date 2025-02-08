import json
import os
from typing import Any


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
