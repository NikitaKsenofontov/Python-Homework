class OwnException(Exception):
    def __init__(self, txt):
        self.txt = txt


result = None
while result is None:
    try:
        num_1, num_2 = int(input('Введите делимое: ')), int(input('Введите делитель: '))
        if num_2 == 0:
            raise OwnException('Делить на 0 нельзя.')
    except OwnException as error:
        print(error)
    except ValueError:
        print('Вы ввели не число.')
    else:
        result = num_1 / num_2
        print(f'{num_1}/{num_2} = {round(result, 1)}')
