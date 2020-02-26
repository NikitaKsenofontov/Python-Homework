def division(numbers):
    numbers = list(map(int, numbers))
    try:
        print(f'{numbers[0]}/{numbers[1]} = {numbers[0] / numbers[1]}')
    except ZeroDivisionError:
        print(f'{numbers[0]}/{numbers[1]} = Делить на 0 нельзя')
    try:
        print(f'{numbers[1]}/{numbers[0]} = {numbers[1] / numbers[0]}')
    except ZeroDivisionError:
        print(f'{numbers[1]}/{numbers[0]} = Делить на 0 нельзя')


user_numbers = input('Введите два числа через пробел: ').split()
division(user_numbers)
