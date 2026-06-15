# ------------------------ Base Conversion function
# decimal -> base 10 {0,1,2,3,4,5,6,7,8,9}
# binary ->  base 2 {0,1}
# octal -> base 8  {0,1,2,3,4,5,6,7}
# decimal -> base 16 {0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F}


# # bUILT -IN FUNCTION
# bin(int) , oct(int) , hex(int)
# all of them return string type
# 10 -> '0o12'
# 10 -> '0xA'
x = 10
print(bin(x))
print(oct(x))
print(hex(x))
print(type(oct(x))) # -> <class 'str'>

# ---------------------------- type convertion

print(int('23423')) # -> 23423
print(int(True))
print(int('0b1010',2))  # (literal , base) like for binary , oct hex
print(int('0xA',16))


print(float(23)) # 23.0

# bool(anything) -> true
# bool(False) , bool(0) , bool()  -> all False

# str(anything) -> string
y = str(5867658)
print(y,type(y))  # 5867658 <class 'str'>

