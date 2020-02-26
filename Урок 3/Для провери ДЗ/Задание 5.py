user_numbers = 0
result = 0
stop = 0

while True:
    if stop == 1:
        print(f'Программа завершена')
        break
    else:
        user_numbers = input('Введите несколько чисел через пробел, для завершения программы введите "q": ').split()
        for i in user_numbers:
            if i == 'q':
                stop = 1
                break
            else:
                result += int(i)
        print(f'Сумма всех введенных чисел - {result}')
