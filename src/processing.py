def filter_by_state(input_date: list[dict[str | int: str]], sorted_key="EXECUTED") -> list[dict[str | int: str]]:
    """
     Функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
     Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению.
    """
    output_data = []
    for i in range(len(input_date)):
        if input_date[i]["state"] == sorted_key:
            output_data.append(input_date[i])
    return output_data
