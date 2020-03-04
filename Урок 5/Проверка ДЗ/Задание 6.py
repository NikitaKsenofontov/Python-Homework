university = {}
lessons_number = 0

with open('courses.txt', 'r', encoding='utf-8') as courses:
    for line in courses:
        content = line.split()
        for string in content[1:]:
            numbers = ''.join([i for i in string if i.isdigit()])
            lessons_number += int(numbers) if numbers.isdigit() else 0
            courses_dict = {el: lessons_number for el in content if el.istitle()}
        university.update(courses_dict)
        lessons_number = 0
    print(university)

