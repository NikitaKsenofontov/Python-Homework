from math import factorial


def fibo_gen(limit):
    for i in range(limit):
        yield factorial(i)


for el in fibo_gen(limit=15):
    print(el)
