num1 = input('Enter number 1: ')
num1 = float(num1)
num2 = input('Enter number 2: ')
num2 = float(num2)
if num1 < num2:
    print(num1, 'is smaller')
elif num2 < num1:
    print(num2,'is smaller')
else:
    print(num1,' and ',num2,'are the same')
