'''
Immutable integer
'''

i = 9999
def update_int(i):
    i += 1
    print("Immutable int inside", i, id(i))
print("Immutable int outside", i, id(i))
update_int(i)
print("Immutable int outside", i, id(i))