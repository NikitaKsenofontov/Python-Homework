class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def change_type(cls, data):
        return f'День {int(data[0]):02d}, Месяц {int(data[1]):02d}, Год {int(data[2])}'

    @staticmethod
    def validation(data):
        if not int(data[0]) in range(1, 32) or not int(data[1]) in range(1, 13) or int(data[2]) > 2020:
            return 'Введена некоррекная дата!'

    def data_func(self):
        result_1 = Data.change_type(self.data.split('-'))
        result_2 = Data.validation(self.data.split('-'))
        return result_2 if result_2 else f'Переформатированная дата (тип int)\n{result_1}'


user_data = input('Введите дату (чч-мм-гг): ')
mc = Data(user_data)
print(mc.data_func())
