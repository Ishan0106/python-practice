# Inquiry methods -> return true or false
# isalpha
# islower
# isupper
# istitle

s = 'Hello'
print(s.isalpha())
print(s.islower())
print(s.isupper())
print(s.istitle())

# True
# False
# False
# True

s1 = 'Hello Dear'
print(s1.istitle())

# true

s3 = ' '
print(s3.isspace())

# true)

s4 = '\n\v'
print(s4.isprintable())
# false

s5 = '4h'
print(s5.isidentifier())
# false

s6 = '24234'
print(s6.isnumeric())
# true   only for numbers no decimal or alpha

s7 = '445'
print(s7.isdigit())
# true

s8 = '54.67'
print(s8.isdigit())
# false

print(s8.isdecimal())
# true

print(s7.isdecimal())
#true

s9 = 'wefverv4'
print(s9.isascii())
# true
# isascii() return true if every character belongs to the ascii set (0 - 127)
