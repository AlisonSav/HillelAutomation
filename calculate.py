import operator

actions = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '//': operator.floordiv,
    '%': operator.mod,
    '**': operator.pow,
}
x = float(input('Enter X: '))
action = input('Enter action: ')
y = float(input('Enter Y: '))
if y == 0 and action in ['/', '//', '%']:
    print('Error! Division by zero!')
else:
    func = actions.get(action)
    if not action:
        print('Not supported action')
    else:
        print(func(x, y))
