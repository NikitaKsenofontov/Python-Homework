number_of_elements = int(input('Укажите желаемую длинну списка: '))

if number_of_elements < 0:  # Проверка на корректность ввода
    number_of_elements = int(input('Необходимо указать положительное число: '))

my_list = []
index_of_element = 0

while index_of_element < number_of_elements:  # Заполнение списка
    element = input(f'Введите {index_of_element + 1}-й элемент списка: ')
    my_list.append(element)
    index_of_element += 1

print(f'Стартовый список:\n{my_list}')

new_list = my_list[1:len(my_list)-1:2]  # Вырезаем необходимые элементы

index = 0

for i in my_list[:len(my_list):2]:  # Ротация соседних элементов
    new_list.insert(index + 1, i)
    index += 2

# Чтобы не выбрасывался последний элемент по нечетному индексу если кол-во элементов списка четное
if len(my_list) % 2 == 0:
    new_list.insert(-1, my_list[-1])

my_list = new_list
print(f'Преобразованный список:\n{my_list}')
