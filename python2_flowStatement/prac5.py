# # for loop 
# # range(star,stop,step) -> step, star    ->     toptional  
# # stop excluded

# # range(5) -> 0,1,2,3,4,
# range(1,5) -> 1 se 4
# range(6,11) -> 6 se 10
# range(0,10,2) -> 0 , 2 , 4 , 6 , 8 

# range(-5,-1) -> -5 se -2
# range(-2,3) -> -2 se 2

# range(10,5,-1) -> 10 se 6 

for i in range(2,9):
    print(i,end=',')

for x in 'fvdvdfvd':
    print(x)

# Fibonacci
a = 0
b = 1
n = 5
for i in range(n):
    c = a + b
    a = b
    b = c
    if i == n-3:
        print(c)


0,1,1,2,3,5,8

# Pass
for i in range(4):
    pass
# when you dont have anything to write in loop
# can be use with if ....
# generally pass is use to make some delay

# nested for loop
for i in range(3):
    for j in range(4):
        print(i,'-',j,end = ' ')
    print('')