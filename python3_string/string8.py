# Case conversion
#------------------------> capitalise
s1 = 'hello dear'
s2 = s1.capitalize()
print(s2) #-> Hello dear

# below about capitalise it will make sure only first letter should be capitalise
s3 = 'hello Dear'
s4 = s3.capitalize()
print(s3) #->Hello dear

#-------------------------> upper
s5 = s1.upper()
print(s5) # HELLO DEAR

#-------------------------> lower               
s6 = s1.lower()
print(s6) # hello dear

#--------------------------> tilte
s7 = s1.title()
print(s7) # Hello Dear

#---------------------------> swapcase
s8 = s1.swapcase()
print(s8) # HELLO DEAR

#---------------------------> casefold
s9 = s1.casefold()
print(s9) # hello dear   its like lower only
# casefold goes further designed for case insensitive conversions as well