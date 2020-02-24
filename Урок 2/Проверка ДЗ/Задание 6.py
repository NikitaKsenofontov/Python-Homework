goods = []
goods_el = []
features = {'название': '', 'цвет': '', 'стоимость': '', 'количество': ''}
analytics = {'название': [], 'цвет': [], 'стоимость': [], 'количество': []}
num = 0

number_of_products = int(input('Введите желаемое кол-во продуктов для заполнения: '))

while num < number_of_products:
    for key in features.keys():
        value = input(f'Введите {key} {num + 1}-го продукта: ')
        features[key] = value
    goods_el = (num + 1, features.copy())
    goods.append(tuple(goods_el))
    num += 1

print(goods)
