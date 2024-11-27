# Импорт модулей
from src.widget import get_date, mask_account_card

# Ввод данных для маскировки и вывод результата
while True:
    user_input = input("Введите тип и номер карты или счет с номером: ")
    output_mask = mask_account_card(user_input)
    if "Ошибка" in output_mask:
        print("Введены некорректные данные, попробуйте еще раз!")
        continue
    else:
        break

print(output_mask)

# Проверка функции get_data()
print(get_date("2024-03-11T02:26:18.671407"))
