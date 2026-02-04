QUESTION = input('Do you want to convert Fahrenheit to Celsius or Celsius to Fahrenheit:')
if QUESTION == 'Fahrenheit to Celsius':
    Fahrenheit = input('Enter Fahrenheit: ')
    Fahrenheit = float(Fahrenheit)
    Celsius = ((Fahrenheit -32) *1.8)
    print('The Celsius of',Fahrenheit,'°F is',Celsius,'°C')
elif QUESTION == 'Celsius to Fahrenheit':
    Celsius1 = input('Enter Celsius: ')
    Celsius1 = float(Celsius1)
    Fahrenheit1 = ((Celsius1 * 1.8) +32)
    print('The Fahrenheit of',Celsius1,'°C is',Fahrenheit1,'°F')
else:
    print('ERROR')