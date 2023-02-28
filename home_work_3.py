""" Homework 3 """
command = input('Start! Enter command: ')
commands_list = ['add', 'earliest', 'latest', 'shortest', 'longest']
working_list = []
while True:
    if command == 'add':
        value = input('Enter your value for your list: ')
        working_list.append(value)
    elif command == 'earliest':
        # виводить збережені нотатки у хронологічному порядку - від найстарішої до найновішої
        print(working_list)
    elif command == 'latest':
        # виводить збережені нотатки у хронологічному порядку - від найновішої до найстарішої
        print(working_list[::-1])
    elif command == 'longest':
        # виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої
        working_list.sort(key=len, reverse=True)
        print(working_list)
    elif command == 'shortest':
        # виводить збережені нотатки у порядку їх довжини - від найкоротшої до найдовшої
        working_list.sort(key=len)
        print(working_list)
    elif command not in commands_list:
        # negative case
        print('You have entered invalid command')
    elif command == 'exit':
        # stop the programm
        break
    command = input('Enter command: ')
print('Program has stopped')
