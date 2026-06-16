# prefix and suffix

s = 'python is crazy'
print(s.startswith('py')) #-> true
print(s.startswith('is',7)) #-> true
      
print(s.endswith('crazy')) #->true


s1 = s.removeprefix('py') # will give a new string
print(s1) # thon is crazy

# similarly for suffix

# partition
s4 = 'python is crazy'
s5 = s4.partition('is') #-> return tuple
print(s5) #('python ', 'is', ' crazy')
# Note with split() it will not give 'is' in the answer
# split return list
w = 'saxsxaxsaeec'
print(w.split('a'))

