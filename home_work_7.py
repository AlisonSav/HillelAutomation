import json

with open('domains.json', 'r') as read_file:
    data = read_file.read()
data = data.replace('\n', '')
data = data.split('.')
my_list = []
for i in data:
    my_list.append(i)
print(my_list[1:])

with open('authors.txt', 'r') as js_file:
    file = js_file.readlines()
    print(file)
l = [1, 2, 3, 3, 2, 4, 6]


def main(lst):
    dct = {}
    lst_set = set(lst)
    for i in lst_set:
        dct[i] = lst.count(i)
    return dct


print(main(l))
