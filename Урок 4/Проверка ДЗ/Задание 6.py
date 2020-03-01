from itertools import count, cycle

my_list = [3, 9, 4, 5, 6]
count_list = []
repeat_list = []
step = 0

for el in count(1):
    if el > 20:
        break
    count_list.append(el)

for el in cycle([3, 9, 4, 5, 6]):
    if step > (len(my_list) * 2 - 1):
        break
    repeat_list.append(el)
    step += 1

print(count_list)
print(repeat_list)
