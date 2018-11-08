# Not the same as primitive vs object in JavaScript.
# Everything in Python is an object. Consider isinstance(1, object)  == True

'''
Mutable
'''
scaryThings = ['spiders', 'Cruella de Vil']

def inspireFear(scaryThings):
    print('mutable inside function', id(scaryThings))
    scaryThings.append('nobody ever using Interview Cake')
    scaryThings.append('i should have gotten a real job')
    scaryThings.append('why am i doing this to myself')
    print('mutable inside function', id(scaryThings))

print('mutable outside function', id(scaryThings))
inspireFear(scaryThings)
print('mutable outside function', id(scaryThings))
print(scaryThings)
scaryThings += ['abc']
print('mutable outside function', id(scaryThings))
print()


'''
Immutable
'''
s = 'abcdef'
def modify_string(s):
    print('immutable string inside function', id(s))
    s += 'xyz'
    print('immutable string inside function', id(s))

print('immutable string outside function', id(s))
modify_string(s)
print('immutable string outside function', id(s))
print(s)
print()



'''
Immutable
'''

threatLevel = 99999

def inspireFear(threatLevel):
    print('immutable inside function', id(threatLevel))
    threatLevel += 100
    print('immutable inside function', id(threatLevel))


print('immutable outside function', id(threatLevel))
inspireFear(threatLevel)
print('immutable outside function', id(threatLevel))
print(threatLevel) # Whoops! It's still 1!


