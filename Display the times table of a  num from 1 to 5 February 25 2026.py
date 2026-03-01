number = input('Enter a number: ')
number = int(number)
for x in range(1,6):
    answer = x * number
    print(x,'*',number,'=',answer)