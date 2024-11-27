from src.widget import mask_account_card

while True:
    user_input = input("Введите тип и номер карты или счет с номером: ")
    output_mask = mask_account_card(user_input)
    if "Ошибка" in output_mask:
        print("Введены некорректные данные, попробуйте еще раз!")
        continue
    else:
        break

print(output_mask)