myList = [0,1,2]
myBytes = bytes(myList)
print(myBytes)
print(list(myBytes))
myString = "mine"
try:
    print(bytes(myString))
except Exception as e:
    print(e)
    print(e.args[0])

a = type(myString)
print(type(myString))
print('\'str\'' in str(a))
print(type("") == type(a))
