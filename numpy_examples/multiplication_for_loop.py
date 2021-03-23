import numpy as np

print("Multiplication with For Loop")
print()

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

# out = [([0] * len(Y[0]))] * len(X)
out = [[0, 0],[0, 0],[0, 0]]
# out = []
out = [[0] * 2 for i in range(3)]

print('X')
print(X)
print('Y')
print(Y)
print('Product')


for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            jjj = X[i][k] * Y[k][j]
            out[i][j] += X[i][k] * Y[k][j]


print(np.array(out))
