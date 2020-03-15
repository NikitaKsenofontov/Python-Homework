from random import randint


class OwnException(Exception):
    def __init__(self, txt):
        self.txt = txt


class OfficeEquipment:
    sku_list = []

    def __init__(self, name, model, price, stock, sales):
        self.name = name
        self.model = model
        self.price = price
        self.stock = stock
        self.sales = sales

    @staticmethod
    def sku_gen():
        sku = []
        for _ in range(6):
            sku.append(randint(0, 9))
        return ''.join(str(i) for i in sku)

    @property
    def sku_add(self):
        sku = OfficeEquipment.sku_gen()
        self.sku_list.append(OfficeEquipment.sku_gen())
        return sku

    def buy(self, quantity):
        self.stock += int(quantity)
        return self.stock

    def sell(self, quantity):
        self.stock -= int(quantity)
        self.sales += int(quantity)
        return self.stock, self.sales


class Validations:

    @staticmethod
    def validate(quantity):
        try:
            if quantity.isalpha() or quantity == '':
                raise OwnException('Ошибка! Введено не число.')
            elif quantity.startswith('0'):
                raise OwnException('Ошибка! Кол-во не может начинаться с нуля.')
            elif int(quantity) < 0:
                raise OwnException('Ошибка! Введено отрицательное число.')
        except OwnException as error:
            return error
        else:
            return None


class Equipment(OfficeEquipment, Validations):
    def __init__(self, name, model, price, stock, sales):
        self.sku = OfficeEquipment.sku_gen()
        OfficeEquipment.__init__(self, name, model, price, stock, sales)

    @property
    def data(self):
        data = {'Sku': self.sku, 'Name': self.name, 'Model': self.model,
                'Price': self.price, 'Stock': self.stock, 'Sales': self.sales}
        return data

    def buy(self, quantity):
        result = Validations.validate(quantity)
        if result is not None:
            return result
        else:
            OfficeEquipment.buy(self, quantity)
        return self.stock

    def sell(self, quantity):
        result = Validations.validate(quantity)
        if result is not None:
            return result
        else:
            if int(quantity) > self.stock:
                return f'Отклонено! Доступное кол-во к продаже {self.stock}шт.'
            OfficeEquipment.sell(self, quantity)
        return self.stock, self.sales


good_1 = Equipment('Принтер', 'Epson', 19990, 38, 15)
good_2 = Equipment('Принтер', 'HP', 31990, 42, 0)
good_3 = Equipment('Сканер', 'Canon', 9990, 17, 6)
good_4 = Equipment('Сканер', 'HP', 23990, 8, 1)
good_5 = Equipment('Ксерокс', 'Xerox', 32990, 0, 38)
good_6 = Equipment('Ксерокс', 'Kyocera', 27990, 51, 25)
all_goods = [good_1.data, good_2.data, good_3.data, good_4.data, good_5.data, good_6.data]
goods_list = [good_1, good_2, good_3, good_4, good_5, good_6]


def all_good_list():
    print('Список всех товаров:')
    for good in all_goods:
        print(good)
    print('-' * 50)


def sku_seek(sku):
    step = 0
    while step < len(all_goods):
        good = all_goods[step]
        if sku == good['Sku']:
            return step
        step += 1
    else:
        print('Ошибка! Артикула с таким номером не существует.')


print('Добро пожаловать!')
all_good_list()
while True:
    user_input = input('Введите наименование операции, которую хотите совершить ("купить", "продать", "список")\n'
                       'Для завершения программы введите "q": ')
    if user_input == 'q':
        all_good_list()
        print('Работа программы завершена.')
        break
    elif user_input == 'список':
        all_good_list()
    elif user_input == 'купить' or user_input == 'продать':
        user_sku = input('Введите артикул товара: ')
        res = sku_seek(user_sku)
        while res is None:
            user_sku = input('Введите артикул товара: ')
            res = sku_seek(user_sku)
        if user_input == 'купить':
            user_quantity = input('Введите кол-во к покупке: ')
            end = goods_list[res].buy(user_quantity)
            if not str(end).isdigit():
                print(end)
            all_goods = [good_1.data, good_2.data, good_3.data, good_4.data, good_5.data, good_6.data]
            print('Операция завершена.')
            print('-' * 50)
        elif user_input == 'продать':
            user_quantity = input('Введите кол-во к продаже: ')
            end_1, end_2 = goods_list[res].sell(user_quantity)
            if not str(end_1).isdigit():
                print(end_1)
            all_goods = [good_1.data, good_2.data, good_3.data, good_4.data, good_5.data, good_6.data]
            print('Операция завершена.')
            print('-' * 50)
    else:
        print('Неккоректный ввод!')
