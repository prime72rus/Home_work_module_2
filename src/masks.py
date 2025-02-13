import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX
    """
    if len(card_number) != 16 or not card_number.isdigit():
        logger.error(f"{get_mask_card_number.__name__} Ошибка: некорректные данные")
        raise ValueError("Недопустимые вводные данные")
    logger.info(f"{get_mask_card_number.__name__} Маскирование номера карты")
    return card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[12:]


def get_mask_account(account_number: str) -> str:
    """
    Функция принимает на вход номер счета в виде числа и возвращает маску номера по правилу
    **XXXX
    """
    if len(account_number) != 20 or not account_number.isdigit():
        logger.error(f"{get_mask_account.__name__} Ошибка: некорректные данные")
        raise ValueError("Недопустимые вводные данные")
    logger.info(f"{get_mask_account.__name__} Маскирование номера счета")
    return "**" + account_number[-4:]
