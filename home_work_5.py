from functools import reduce
from random import randint, choice
import string

# Ex_1
# я не понимаю, как это делать.

# Ex_2
domains = ['net', 'com', 'ua']
names = ['king', 'miller', 'alex']
letters = string.ascii_lowercase


def create_email(name, domain):
    part_1 = choice(name)
    part_2 = randint(100, 1000)
    part_3 = ''.join(choice(letters) for _ in range(randint(5, 8)))
    part_4 = choice(domain)
    return str(part_1) + '.' + str(part_2) + '@' + str(part_3) + '.' + str(part_4)


print(create_email(names, domains))

# Lambda ex_1
inters_for_two = lambda tup1, tup2: tup1.intersection(tup2)
print(f'Intersection of two sets is: {inters_for_two({1, 2, 3, 4}, {3, 4, 5, 6})}')

# Lambda ex_2
is_number = lambda x: isinstance(x, (int, float))
print(is_number(5))
print(is_number(1.25))
print(is_number('ololo'))

# Lambda ex_3
list_1 = [20, 43, 12, 94, 2, 67, 43]
min_value = reduce(lambda x, y: x if x < y else y, list_1)
max_value = reduce(lambda x, y: x if x > y else y, list_1)
print(f'Min value from list_1 is: {min_value}')
print(f'Max value from list_1 is: {max_value}')

# Lambda ex_4
my_list = [3, 6, 2, 9, 4, 6, 1, 1, 0, 6]
summ = reduce(lambda x, y: x + y, my_list)
print(f'The sum of my list is : {summ}')
