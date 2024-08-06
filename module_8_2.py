# Сложные моменты и исключения в стеке вызовов функции". Цель: понять как работают исключения внутри функций
# и как обрабатываются эти исключения на практике при помощи try-except.


def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for num in numbers:
        try:
            result += num
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {num}')
            incorrect_data += 1
    print(f'Кол-во некорректных данных: {incorrect_data}')
    return result, incorrect_data


def calculate_average(numbers):
    try:
        result, incorrect_data = personal_sum(numbers)  # вызываем personal_sum и передаем аргумент numbers

        # подсчет количества корректных чисел
        correct_num = len(numbers) - incorrect_data

        if correct_num == 0:
            raise ZeroDivisionError
        return result / correct_num  # Делим на количество корректных чисел
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


# Примеры вызова функции calculate_average
print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
