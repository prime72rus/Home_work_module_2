def get_user_input(number_of_digits: int) -> str:
    """
    Функция принимает на вход длину номера для проверки соответствия ввода,
    выполняется ввод числа с проверкой требований и возвращает введенное число при условии корректного ввода
    """
    while True:
        user_input_number = input(f"Введите {number_of_digits}-ти значный номер: ")
        if not user_input_number.isdigit():
            print("Ошибка! Введено нечисловое значение")
            continue
        elif user_input_number[0] == "0":
            print('Ошибка! Номер не может начинаться с "0"')
            continue
        elif len(user_input_number) < number_of_digits:
            print("Ошибка! Введено недостаточно цифр номера!")
            continue
        elif len(user_input_number) > number_of_digits:
            print("Ошибка! Превышено количество цифр номера!")
            continue
        else:
            break
    return user_input_number
