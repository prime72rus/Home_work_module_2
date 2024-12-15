from typing import Dict, List

from src.widget import format_date_is_correct


def filter_by_state(
        input_data_for_filter: List[Dict[str, str | int]], target_state: str = "EXECUTED"
) -> List[Dict[str, str | int]] | None:
    """
    Функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    output_data = []
    for data_item in input_data_for_filter:
        if "state" not in data_item.keys():
            raise KeyError
        elif data_item["state"] == target_state:
            output_data.append(data_item)
    return output_data


def sort_by_date(
        input_data_for_sorted: List[Dict[str, str | int]], sorted_param: bool = True
) -> List[Dict[str, str | int]] | None:
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
