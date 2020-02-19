first_day_result = int(input('Результат спортсмена в первый день, км: '))
goal = int(input('Желаемая цель, км: '))

while first_day_result < 0 or goal < 0:
    print('Значения в киллометрах не могут быть отрицательными.')
    first_day_result = int(input('Результат спортсмена в первый день, км: '))
    goal = int(input('Желаемая цель, км: '))

progress = first_day_result

if first_day_result >= goal:
    print('Вы уже достигли своей цели!')
else:
    increase = 0.10
    day = 0

    while progress < goal:
        progress = progress + progress * increase
        day += 1
        print(f'{day}-й день - {progress:.2f} км.')

    print(f'На {day}-й день вы достигните своей цели, ваш результат будет {progress:.2f} км.')
