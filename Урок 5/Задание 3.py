wages = []

try:
    with open('Salary.txt', 'r', encoding='utf-8') as user_file:
        print('Следующие сотрудники имеют зарплату менее 20 000р.:')
        for line in user_file:
            name, salary = line.split()
            if int(salary) < 20000:
                print(f'{name} - {salary}')
            wages.append(int(salary))
        print(f'Средний доход сотрудников - {sum(wages)/len(wages):.0f}')
except FileNotFoundError:
    print(f'Файл не найден')
