# String concatenation
s = 'avc'
# print(s + 10) # -> error (cannot with int)
print(s + '29')
s = s + str(10)
s = 'dsf' + 'asda'
s = 'a' * 5 #-> 'aaaaa'

# bool < int < float < complex

# Conditional statement 
# < , <= , >= , == , !=

# Conditional statement
a = 9
b= 0
if(a < b):
    print('yeah')
else:
    print('dvsdv')

# Logical operator
# and, or ,not
a = 1
b = 2
c = 3
if a > b or b > 2:
    print('sdvsdvsa')
else:
    print('dsda')

if not a > b:
    print('sdacsdvv')
else:
    print('dsvasdv')


ch = input('Enter your chararcter')
if(ch in ['a','e','i','o','u']):
    print('vowel')
else:
    print('consonent')

if ch == 'a':
    print('sdcsadcasdcc')
elif ch == 'e':
    print('sdcascac')
else:
    print('dscdsvdvsdav')


