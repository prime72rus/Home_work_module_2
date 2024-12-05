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

    if len(number) == card_number_length and number.isdigit():
        output_data = f"{name} {get_mask_card_number(number)}"
    elif len(number) == account_number_length and number.isdigit():
        output_data = f"{name} {get_mask_account(number)}"
    else:
        output_data = "Ошибка"
    return output_data


def get_date(no_formating_date: str) -> str:
    """
    Функция принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    formating_date = ".".join(reversed(no_formating_date.split("T")[0].split("-")))
    return formating_date
