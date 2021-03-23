import numpy as np

X = \
    [
        [3, 2, 8],
        [3, 3, 4],
        [7, 2, 5]
    ]

Y = \
    [
        [2, 3],
        [4, 2],
        [5, 5]
    ]

X = np.array(X)
Y = np.array(Y)

print("INPUT MATRICES")
print("X")
print(X)
print("Y")
print(Y)
print()
print("DOT PRODUCT")
print(np.dot(X, Y))
print()
print("CROSS PRODUCT")
print(np.cross(X, Y))





