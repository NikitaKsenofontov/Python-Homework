my_list = [20, 12, 11, 7, 7, 5, 3, 3, 1]

number = int(input('Введите положительное целое число: '))

if number < 0:
    number = int(input('Введите положительное целое число: '))

for i in my_list:
    if number == i:
        amount_of_similar_el = my_list.count(i)
        index_of_el = my_list.index(i)
        my_list.insert(index_of_el + amount_of_similar_el, number)
        break
    elif number > max(my_list):
        my_list.insert(0, number)
        break
    elif number < my_list[-1]:
        my_list.append(number)
        break
    elif number > i:
        my_list.insert(my_list.index(i), number)
        break

print(my_list)
