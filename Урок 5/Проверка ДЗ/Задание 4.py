with open('Translated_numbers', 'w', encoding='utf-8') as user_translate:
    print(f'Файл {user_translate.name} готов к редактированию.')
    with open('Numbers.txt', 'r') as numbers:
        for line in numbers:
            translation = lambda *args: input(f'Введите перевод слова {args[0][0]}: ')
            new_word = translation(line.split())
            user_translate.writelines(line.replace(line.split()[0], new_word))
    print(f'Редактирование файла {user_translate.name} Завершено.')
