# Решение через список
name_of_months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
                  'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
number_of_months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

number = int(input('Введите номер месяца: '))

if number in number_of_months:
    month = name_of_months[number-1]
    print(month)
else:
    print('Такого месяца нет!')

# Решение через список
months = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль',
          8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}

number = int(input('Введите номер месяца: '))

if number in months.keys():
    month = months.get(number)
    print(month)
else:
    print('Такого месяца нет!')
