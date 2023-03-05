# Ex_1
list_1 = [1, 7, 11, 2, 3, 3, 4, 0, 5, 6]
list_2 = [4, 5, 0, 7, 1, 6, 7, 8]
set_3 = set(list_1).intersection(set(list_2))
print(f'Intersection is: {set_3}')

# Ex_2
students = {'Alis': 11, 'Anton': 10, 'Dima': 8, 'Sasha': 9, 'Lera': 5, 'Andriy': 12}
good_students = []
avg_score = sum(students.values()) / len(students)
for key, value in students.items():
    if value > avg_score:
        good_students.append(key)
print(f'Students with good scores are: {good_students}')

# Ex_3
my_list = [1, 3, 5, 2, 9, 6, 1, 0, 6, 8, 9, 5, 4, 6, 3, 1, 0]
new_set = set(my_list)
print(f'The number of unic values is: {len(new_set)}')
# Ex_4
str_1 = input('Enter your first list: ')
lst_1 = str_1.split(' ')
str_2 = input('Enter your second list: ')
lst_2 = str_2.split(' ')
lst_3 = lst_1 + lst_2
for i in lst_3:
    print(i)

# Ex_5
some_str = 'one two three one four five seven ten seven one'
# в завдвннi написано - дана строка. про введеня з консолi нiчого не було
some_str = some_str.split(' ')
values_dct = {i: some_str.count(i) for i in some_str}
print(values_dct)
