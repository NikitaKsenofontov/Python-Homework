def division(numbers):
    numbers = list(map(int, numbers))
    return sum(numbers) - min(numbers)


user_numbers = input('Введите три числа через пробел: ').split()
print(f'Сумма наибольших двух чисел: {division(user_numbers)}')
