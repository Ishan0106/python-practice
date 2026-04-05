# reverse and palindrome 

n = 3423412
temp = n
rev = 0
while(n > 0):
    rev = rev * 10 + (n % 10)
    n = n // 10
print('reverse number:',rev)
if temp == rev:
    print('palindrome')
else:
    print('not')