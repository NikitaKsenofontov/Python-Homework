my_string = input('Пожалуйста введите текст из разных слов (без знаков препинания): ')

my_list = my_string.split()

for num, i in enumerate(my_list):
    print(f'{num + 1} - {i[:10]}') if len(i) > 10 else print(f'{num + 1} - {i}')
