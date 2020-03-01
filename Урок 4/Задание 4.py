my_list = [3, 9, 4, 5, 6, 7, 2, 6, 2, 8, 4, 9, 6]

new_list = [i for i in my_list if my_list.count(i) == 1]
print(new_list)
