my_list = [3, 9, 5, 6, 7, 2, 6, 8, 4, 9, 6]

new_list = [i for i in my_list if i > my_list[my_list.index(i)-1]]
print(new_list)
