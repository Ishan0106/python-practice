# Match case 

day = int(input('enter the day'))
match day:
    case 0:
        print('Monday')
    case 1:
        print('Tuesday')
    case 2:
        print('wed')
    case 3:
        print('thurs')
    case 4:
        print('fri')
    case 5:
        print('sat')
    case 6:
        print('sun')
    case _:
        print('invalid')