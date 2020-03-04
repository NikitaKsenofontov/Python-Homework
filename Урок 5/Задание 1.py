try:
    with open('user_text.txt', 'x', encoding="utf-8") as user_file:
        user_file.write('Данные пользователя:\n')
except IOError:
    print('Редактирование существующего файла.')
finally:
    with open('user_text.txt', 'a', encoding="utf-8") as user_file:
        while True:
            text = input("Введите текст, для завершения записи наберите q: ")
            if text == 'q':
                break
            user_file.write(f'{text}\n')
        print(f'Запись завершена, файл "user_text.txt" закрыт.')
