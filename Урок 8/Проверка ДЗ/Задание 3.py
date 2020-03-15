class OwnException(Exception):
    def __init__(self, txt):
        self.txt = txt


def check(data):
    try:
        if data.isalpha() or data == '':
            raise OwnException('Вы ввели не число!')
    except OwnException as error:
        print(error)
    else:
        result.append(data)


result = []
while True:
    user_data = input('Введите элеиент списка, для завершения введите "q": ')
    if user_data == 'q':
        print(f'--------\nРабота программы завершена.\nИтоговый список - {result}')
        break
    check(user_data)
