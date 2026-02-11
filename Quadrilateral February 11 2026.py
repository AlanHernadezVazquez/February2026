AB = input('Enter length 1: ')
AB = float(AB)
BC = input('Enter length 2: ')
BC = float(BC)
CD = input('Enter length 3: ')
CD = float(CD)
DA = input('Enter length 4: ')
DA = float(DA)
I = input('Enter internal angle: ')
I = float(I)
if AB == BC:
    if AB == CD:
        if BC == DA:
            if I == 90:
                print('Its a square')
            else:
                print('Its a rhombus')
        else:
            print('Its an irregular quadrilateral')
    else:
        print('Its an irregular quadrilateral')
else:
    if AB == CD:
        if BC == DA:
            if I == 90:
                print('Its a rectangle')
            else:
                print('Its a parallelogram')
    else:
        print('Its an irregular quadrilateral')
    