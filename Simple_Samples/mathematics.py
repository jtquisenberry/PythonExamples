import math

a = math.pi
list1 = [0,1,2,3,4,5, math.pi/2, math.pi]
b = list(map(math.sin, list1))
print(b)