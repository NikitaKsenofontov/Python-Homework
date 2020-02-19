print('Пожалуйста введите следующие показатели фирмы')
revenue = int(input('Выручка, млн.руб: '))
cost = int(input('Издержки, млн.руб: '))
employee = int(input('Кол-во сотрудников, чел.: '))

if revenue > cost:
    print(f'Компания имеет прибыль в размере {revenue - cost} млн.руб')
    print(f'Рентабельность выручки составила {(revenue - cost) / revenue * 100} %')
    print(f'Прибыль в расчете на одного сотрудника составила {(revenue - cost) / employee * 1000} тыс.руб.')
elif revenue == cost:
    print('Компания находится в точке безубыточности')
else:
    print(f'Компаня терпит убытки в размере {cost - revenue} млн.руб')


