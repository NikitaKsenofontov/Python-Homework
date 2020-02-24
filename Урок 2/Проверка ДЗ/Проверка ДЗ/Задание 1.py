my_list = [None, 'Hello', 10, 2.6, False, [2, 2], (4, 4), {'my', 'your'}, {'key_1': 'value_1', 'key_2': 'value_2'}]

for i, el in enumerate(my_list):
    print(f'{i} - {type(el)}')
