a = input('Enter age: ')
a = int(a)
if a < 12:
    print('Fare is: 2 euros')
elif a > 65:
    v = input('Do you have a travel card: ')
    if v == 'Yes':
        print('Fare is: 0 euro')
    elif v == 'No':
        print('Fare is: 3 euros')
elif a <= 65:
    print('Fare is: 5 euros')