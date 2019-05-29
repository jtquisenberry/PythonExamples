
# zip
# Combine two lists
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(list(zipped))
print()

# unzip
# Break a list into components
x2, y2 = zip(*zip(x, y))
print(x2)
print(y2)
print()

# zip with *
#
q = [(5,6),(7,8),(9,10)]
print(list(zip(*q)))




