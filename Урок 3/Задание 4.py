def get_pow_var3(number, pow_):
    pow_ *= -1
    new_number = number
    step = 1
    while step < pow_:
        new_number *= number
        step += 1
    return 1 / new_number


user_number = int(input('Введите положительное число: '))
while user_number < 0:
    user_number = int(input('Введите положительное число: '))

user_pow = int(input('Введите отрицательную степень: '))
while user_pow >= 0:
    user_pow = int(input('Введите отрицательную степень: '))

get_pow_var1 = lambda number, pow_: number ** pow_
get_pow_var2 = lambda number, pow_: pow(number, pow_)

print(get_pow_var1(user_number, user_pow))
print(get_pow_var2(user_number, user_pow))
print(get_pow_var3(user_number, user_pow))
