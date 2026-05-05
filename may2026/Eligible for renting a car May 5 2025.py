a = input('Enter age: ')
a = int(a)
if a >= 18:
    print('You have a license')
    b = input('Rent a car: ')
    if b == 'Yes':
        print('You can rent a car')
    elif b == 'No':
        print('Okay then')
elif a < 18:
    print('You do not have a license')

