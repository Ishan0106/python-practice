#Alignment and padding
# s.ljust(width,'fill char')
# similarly for ljust, rjust , 


s = 'hello'
print(s.ljust(9))
print(s.ljust(9,'-'))
# hello
# hello----

print(s.rjust(9))
print(s.rjust(9,'-'))

#     hello
# ----hello

print(s.center(9))
print(s.center(9,'-'))

#   hello
# --hello--

print(s.zfill(9))
# print(s.zfill(9,'-')) -> it only taken one argument

# 0000hello



#-----------------------  strip methods

# lstrip() -> remove the spaces if there at the left side of string
# lstrip(char) -> remove the specific character if there at the left side of string

