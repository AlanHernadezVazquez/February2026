QUESTION = input('Do you want to convert Fahrenheit to Celsius or Celsius to Fahrenheit: ')
if QUESTION == 'Fahrenheit to Celsius':
    Fahrenheit = input('Enter Fahrenheit: ')
    Fahrenheit = float(Fahrenheit)
    Celsius = ((Fahrenheit -32) *1.8)
    print('The Celsius of '+str(Fahrenheit)+'°F is '+str(Celsius)+'°C')
elif QUESTION == 'Celsius to Fahrenheit':
    Celsius1 = input('Enter Celsius: ')
    Celsius1 = float(Celsius1)
    Fahrenheit1 = ((Celsius1 * 1.8) +32)
    print('The Fahrenheit of '+str(Celsius1)+'°C is '+str(Fahrenheit1)+'°F')
else:
    print('ERROR')