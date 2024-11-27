from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_data: str) -> str:
    """
    Функция принимает один аргумент - строку, содержащую тип и номер карты или счета.
    Возвращает строку с замаскированным номером.
    """
    card_number_length = 16
    account_number_length = 20

    number_after_split = input_data.split()[-1]
    if len(number_after_split) == card_number_length and number_after_split.isdigit():
        output_data = " ".join(input_data.split()[:-1]) + " " + get_mask_card_number(number_after_split)
    elif len(number_after_split) == account_number_length and number_after_split.isdigit():
        output_data = " ".join(input_data.split()[:-1]) + " " + get_mask_account(number_after_split)
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
