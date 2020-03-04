try:
    with open('text.txt', 'r', encoding='utf-8') as user_file:
        line_number = 0
        for line in user_file:
            line_number += 1
            print(f'Строка - {line_number}, кол-во символов - {len(line)}')
        user_file.seek(0)
        print(f'Итого: строк - {line_number}, символов - {len(user_file.read())}')
except FileNotFoundError:
    print(f'Файл не найден')
