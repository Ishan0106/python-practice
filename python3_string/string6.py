# joining and splitting a string
s1 = 'a-b-c-d-e'
s2 = s1.replace('-','+')
print(s2)   #-> a+b+c+d+e

# s1.replace('-','+',3) -> only three '-' will replace

x = 'ishan@gmail.com'
y = x.replace('gmail','yahoo')
print(y)

# -------------------------join

a = '12'
b = '345'

c = a.join(b)
print(c)  #3124125

# -----------------------------split

s8 = 'grdg&gdvf&grgerg&dgd'
s0 = s8.split('&')
print(s0) #['grdg', 'gdvf', 'grgerg', 'dgd']

# s0 = s8.split('&',3) -> will max split till three positions if find



