

x = 'abcdef'

y = x[0:6]
print(y)
# abcdef

y = x[0:99]
print(y)
# abcdef

y = x[5:-1:-1]
print(y)
#

y = x[5:None:-1]
print(y)
# fedcba

x = list(x)
y = x[5:None:-1]
print(y)
# ['f', 'e', 'd', 'c', 'b', 'a']

x = list(x)
y = x[5:-1:-1]
print(y)
# []

x = list(x)
y = x[5::-1]
print(y)
# ['f', 'e', 'd', 'c', 'b', 'a']