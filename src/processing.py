from typing import Dict, List


def filter_by_state(
    input_data_for_filter: List[Dict[str, str | int]], sorted_key: str = "EXECUTED"
) -> List[Dict[str, str | int]]:
    """
    Функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    output_data = []
    for i in range(len(input_data_for_filter)):
        if input_data_for_filter[i]["state"] == sorted_key:
            output_data.append(input_data_for_filter[i])
    return output_data


def sort_by_date(
    input_data_for_sorted: List[Dict[str, str | int]], sorted_param: bool = True
) -> List[Dict[str, str | int]]:
    """
    Функция принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date).
    """
    sorted_data = sorted(input_data_for_sorted, key=lambda x: x["date"], reverse=sorted_param)
    return sorted_data
