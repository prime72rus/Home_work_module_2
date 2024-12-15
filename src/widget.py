import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_data: str) -> str:
    """
    Функция принимает один аргумент - строку, содержащую тип и номер карты или счета.
    Возвращает строку с замаскированным номером.
    """
    card_number_length = 16
    account_number_length = 20

    parts = input_data.split()
    number = parts.pop()
    name = " ".join(parts)

    if len(number) == card_number_length and number.isdigit() and len(name) > 0:
        return f"{name} {get_mask_card_number(number)}"
    elif len(number) == account_number_length and number.isdigit() and name == "Счет":
        return f"{name} {get_mask_account(number)}"
    else:
        raise ValueError('Недопустимый формат данных')


def get_date(no_formating_date: str) -> str:
    """
    Функция принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    pattern = re.compile(
        r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]+)?([Zz]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?")
    if pattern.match(no_formating_date):
        return ".".join(reversed(no_formating_date.split("T")[0].split("-")))
    else:
        raise ValueError('Недопустимый формат данных')
