import sys

#------------------------------------- Numeric Types--------------
y = 483267458932456938648592
# you can take as my size of int in pyhton
# depending on the data the size is allocated 

print(sys.getsizeof(y))

# Immutable 
x = 34
print(id(x))
x = 56
print(id(x))

# 36
# 140071181093480
# 140071181094184
# variable will be same but it will point to some new location on changing the value
# so like this every data type is immutable changing value will point to new mmemory location


#------------------------------------------Float----------------
a = 89.5
b = 0.056
c = 45E3
# Floating point representation
# a = 12500 -> 125 * 10^2  -> 125E2
# b = 12.34 -> 1234e-2
print(type(c))  # -> <class 'float'>

#-------------------------------------------Bool-----------------
x = True #->1
y = False #->0

#------------------------------------------Complex----------------





