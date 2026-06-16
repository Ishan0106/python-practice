# class string
# find() , index() , endswith() , isalpha() , lower() , upper()

# find(sub,start,end) -> RETURN FIRST INDEX OF SUBSTRING OR -1 IF NOT THERE
# rfind(sub,start,end) it will search from back
# index(sub,start,end)
# rindex(sub,start,end)
# count(sub,start,end) -> count how many times a substring appears

s1 = 'Hello How are you'
x = s1.find('o') #->4
print(x)

print(s1.find('How')) #->6 it will result -1 if not found

if(s1.find('how') == -1):
    print('not found')
else:
    print('found')

print(s1.find('o',5,8)) #-> this will search in range index 5 se 7

x = s1.rfind('o')
print(x)
print(s1.rfind('o',0,15))


# index -> s.index('k') will give error if substring not found 

print(s1.count('o'))