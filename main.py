# Импорт пакетов
from src.masks import get_mask_account, get_mask_card_number
from src.user_input_is_correct import get_user_input

# Объявление констант длины реквизитов карты
CARD_NUMBER_LENGTH = 16
ACCOUNT_NUMBER_LENGTH = 20

# Вызов функций для получения масок номеров реквизитов карты
print("Получение маски номера карты")
mask_card_number = get_mask_card_number(get_user_input(CARD_NUMBER_LENGTH))
print("Получение маски номера счета")
mask_account_number = get_mask_account(get_user_input(ACCOUNT_NUMBER_LENGTH))

# Вывод масок реквизитов на экран
print(f"Маска номера карты: {mask_card_number}")
print(f"Маска номера счета: {mask_account_number}")
