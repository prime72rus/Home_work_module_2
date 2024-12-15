def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX
    """
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError
    return card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[12:]


def get_mask_account(account_number: str) -> str:
    """
    Функция принимает на вход номер счета в виде числа и возвращает маску номера по правилу
    **XXXX
    """
    if len(account_number) != 20 or not account_number.isdigit():
        raise ValueError
    return "**" + account_number[-4:]
