user_number = int(input("Введите число: "))

while user_number < 0:
    user_number = int(input("Введите положительное число: "))

maximum = 0

while user_number > 0:
    num = user_number % 10
    if num > maximum:
        maximum = num
    user_number //= 10

print(f'Максимальное число: {maximum}')
