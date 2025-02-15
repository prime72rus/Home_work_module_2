import re
from collections import Counter

from typing import Any

from src.widget import format_date_is_correct


def filter_by_state(input_data_for_filter: list[Any], target_state: str = "EXECUTED") -> list[Any]:
    """
    Функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    output_data = []
    for data_item in input_data_for_filter:
        if "state" not in data_item.keys():
            continue
        elif data_item["state"] == target_state:
            output_data.append(data_item)
    return output_data


def sort_by_date(input_data_for_sorted: list[Any], sorted_param: bool = True) -> list[Any]:
    """
    Функция принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date).
    """
    for data_item in input_data_for_sorted:
        if "date" not in data_item.keys():
            raise ValueError("Отсутствуют данные для ключа сортировки")
        else:
            if not format_date_is_correct(str(data_item["date"])):
                raise ValueError("Недопустимые данные в значении даты")
    return sorted(input_data_for_sorted, key=lambda x: x["date"], reverse=sorted_param)


def user_input_search(input_data_for_search: list[Any], search_str: str) -> list[Any]:
    """
    Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка.
    Если строка поиска не введена, возвращает исходный список словарей.
    Если совпадений не найдено, возвращает пустой список.
    """
    result = []
    for item in input_data_for_search:
        match = re.search(search_str, item["description"], re.IGNORECASE)
        if match:
            result.append(item)

    return result


def get_count_operation(input_data: list[Any], list_description: list) -> dict:
    """
    Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    """
    temp_list = [item["description"] for item in input_data if item["description"] in list_description]
    result = dict(Counter(temp_list))
    return result
