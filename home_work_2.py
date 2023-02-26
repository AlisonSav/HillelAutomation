from random import randint

# Ex_1
minutes = randint(0, 59)
if 0 <= minutes < 15:
    print(f'{minutes} - First quarter')
elif 15 <= minutes < 30:
    print(f'{minutes} - Second quarter')
elif 30 <= minutes < 45:
    print(f'{minutes} - Third quarter')
elif 45 <= minutes < 60:
    print(f'{minutes} - Fourth quarter')

# Ex_2
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
birth_month = int(input('Enter number of your birth month: '))
if birth_month in winter:
    print('Winter - snow fell outside the window')
elif birth_month in spring:
    print('Spring - everything around bloomed')
elif birth_month in summer:
    print('Summer - children enjoyed summer holidays')
elif birth_month in autumn:
    print('Autumn - everything around lit up with bright colors')
else:
    print('You entered invalid data')

# Ex_3
random_value = randint(100, 100000)
copy_val = random_value
counter = 0
if random_value % 2 == 0:
    while random_value > 0:
        val = random_value % 10
        counter += val
        random_value = random_value // 10
    if counter % 3 == 0:
        print(f'{copy_val} divisible by 6')
    else:
        print(f'{copy_val} not divisible by 6')
else:
    print(f'{copy_val} not divisible by 6')

# Ex_4
x = float(input('Enter x: '))
y = float(input('Enter y: '))
if x == 0:
    print('the point lies on the Y-axis')
elif y == 0:
    print('the point lies on the X-axis')
elif x > 0 and y > 0:
    print('I quarter')
elif x > 0 and y < 0:
    print('IV quarter')
elif x < 0 and y < 0:
    print('III quarter')
elif x < 0 and y > 0:
    print('II quarter')
