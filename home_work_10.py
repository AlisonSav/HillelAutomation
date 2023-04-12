import random


def name(funk):
    print(funk.__name__)
    return funk


@name
def summ(a, b):
    return a + b


@name
def mul(a, b):
    return a * b


my_list = [random.randint(1, 10) for i in range(100)]
print(my_list)

mul(2, 5)
summ(3, 4)
