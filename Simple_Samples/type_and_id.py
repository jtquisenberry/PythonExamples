import inspect

nums = [1,2,3,4,5]
num = 1
string = "abc"

print(nums)
print(type(type(nums)))
print(id(nums))

print(nums.__class__, nums.__class__.__bases__)
print(num.__class__, num.__class__.__bases__)
print(string.__class__, string.__class__.__bases__)

#print(inspect.getmro(nums))
#print(inspect.getmro(num))

string1 = "abc"
string2 = string1
print(id(string1))
print(id(string2))
string1 = "def"
print(id(string1))
print(id(string2))