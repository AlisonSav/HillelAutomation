from math import pi

# Ex1
name = input('Please, enter your name: ')
surname = input('Enter your surname: ')
print(f'Your full name is {name.lower()} {surname.lower()}')
print(f'Your full name is {name.upper()} {surname.upper()}')
print(f'Your full name is {name.title()} {surname.title()}')
# or it can be full_name = name + ' ' + surname, and after full_name.lower() etc.

for _ in range(5):
    print(f'Your full name is {name.title()} {surname.title()}')
# or i can multiply full_name * 5

full_name_2 = '\t' + name + ' ' + surname + '\n' + '\t'
print(full_name_2)
full_name_3 = full_name_2.strip()
# or it can be like this 'full_name_2.lstrip().rstrip()'
print(full_name_3)


# Ex2
def kolo():
    r = float(input('Enter radius of the circle: '))
    length = 2 * pi * r
    s = pi * r ** 2
    print(f'The length of the circle is {round(length, 3)}. The area of the circle is {round(s, 3)}.')
    # added rounding, because the numbers are very large


kolo()


# Ex3
def currency():
    count_dollars = int(input('How many dollars you have? '))
    current_rate = 41.58
    hrn_rate = count_dollars * current_rate
    print(f'For {count_dollars} dollars you can get {round(hrn_rate, 2)} hriven')


currency()
