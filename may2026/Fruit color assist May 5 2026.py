c_i = input('Enter color of item: ')
c_i = str(c_i)
if c_i == 'red':
    fruit = input('Is it a fruit: ')
    if fruit == 'Yes':
        print('It it could be a tomato or apple')
    elif fruit == 'No':
        print('Is it a rose?')
    else:
        print('Invalid')
elif c_i == 'yellow':
    fruit2 = input('Is it a fruit: ')
    if fruit2 == 'Yes':
        print('It could be a banana')
    elif fruit2 == 'No':
        print('Its could be corn or marigold')
else:
    print('ERR0R: PROGRAM CANNOT ASSIST')
        
    