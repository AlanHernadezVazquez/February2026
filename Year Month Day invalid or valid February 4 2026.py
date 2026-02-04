year = input('Enter year: ')
year = int(year)
if year < 0:
    print('Year is invalid')
elif year >= 0:
    print('Year is valid')
month = input('Enter month: ')
month = int(month)
if month < 1:
    print('Month is invalid')
elif month >12:
    print('Month is invalid')
elif month >=1:
    print('Month is valid')
day = input('Enter day: ')
day = int(day)
if day <1:
    print('Day is invalid')
elif day >30:
    print('Day is invalid')
elif month >=1:
    print('Day is valid')