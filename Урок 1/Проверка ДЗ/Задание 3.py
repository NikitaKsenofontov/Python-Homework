user_number = input("Введите число: ")

while int(user_number) < 0:
    user_number = input("Введите положительное число: ")

result = int(user_number) + int(user_number + user_number) + int(user_number + user_number + user_number)

print(f'Результат вычислений: {result}')
