from random import randint  # Чтобы кол-во и набор чисел каждый раз были случайными

q_numbers = randint(5, 10)
step = 0

with open('numbers.txt', 'w+') as random_numbers:
    while step < q_numbers:
        random_numbers.write(f'{randint(1, 10)} ')
        step += 1
    random_numbers.seek(0)
    print(f'Результат записи: {random_numbers.read()}')
    random_numbers.seek(0)
    content = sum(map(int, random_numbers.readline().split()))

print(f'Сумма записанных чисел - {content}')
