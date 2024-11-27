def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX
    """
    mask_card = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[12:]
    return mask_card


def get_mask_account(account_number: str) -> str:
    """
    Функция принимает на вход номер счета в виде числа и возвращает маску номера по правилу
    **XXXX
    """
    mask_account = "**" + account_number[-4:]
    return mask_account
