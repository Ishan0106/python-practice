s1 = 'Hello'
# also supports -ve ase well as +ve indexes
print(s1[3])
print(s1[-5])

# 0   1   2   3   4
# H   e   l   l   o
# -5  -4  -3  -2  -1

# length of string
print(len(s1))

# traversing
for x in s1:
    print(x)

for i in range(len(s1)):
    print(s1[i])

# representation
'rcsfvs'
"fwevewv's"
'''egwgtvrb'''

# Indexing and slicing and immutable
s1 = 'Hello World'

# s[3] = 'r' -> not possible
# slicing
# string[start:end:step]
print(s1[3:7]) #-> 3 se 6 
print(s1[:7]) #-> 0 se 6
print(s1[:]) #-> 0 se last pura
print(s1[-5:-2]) #-> -5 se -3 wor # givr -ve index but in forward direction
print(s1[2:8:2]) #-> alternative letter 
print(s1[::]) 
print(s1[::2])

print(s1[::-1]) #-> negative step will work in backward direction
print(s1[8:2:-1])
print(s1[-1:-5:-1]) # when negative step give start and stop from bakward direction
