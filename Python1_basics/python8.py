# String Comparison
# compare like in dectionary 
'apply' > 'apple'
'cat' < 'catch'
'data' > 'Data' # upper come first than lower
'2nd' < 'Byte' # number comes first


# 0<1<2<3...... < A<B<C.......<a<b<c -> remember

# Bitwise Operator
# they perform operation on the binary representation
a = 10
print(format(a,'b')) #-> to show binary form of 'a' -> 1010
print(a.bit_length()) # -> 4

c = 13

print(a&c) # 1010 & 1101 -> 1000 -> 8

# XOR
# 1 ^ 1 -> 0
# 1 ^ 0 -> 1
# 0 ^ 1 -> 1
# 0 ^ 0 -> 0

# left shift
# a << 1
# a -> 1010 -> 10100 -> 20 -> 2 * a

# a << 2 -> 101000 -> 40  -> 2**2 * a

# a << 5 -> 2**5 * a

# a << x -> 2**x * a

# right shift

# a >> x -> a // 2**x
