""" Homework 3 """
command = input('Start! Enter command: ')
working_list = []
while True:
    if command == 'add':
        value = input('Enter your value for your list: ')
        working_list.append(value)
    elif command == 'earliest':
        print(working_list)
    elif command == 'latest':
        print(working_list[::-1])
    elif command == 'longest':
        working_list.sort(key=len, reverse=True)
        print(working_list)
    elif command == 'shortest':
        working_list.sort(key=len)
        print(working_list)
    elif command == 'exit':
        break
    command = input('Enter command: ')
print('Program has stopped')
