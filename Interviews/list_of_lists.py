rows = 3
cols = 4

mat = []
for i in range(rows):
    mat.append([0] * cols)

mat[0][1] = 9

print(mat)

mat2 = [[0 for x in range(cols)] for x in range(rows)]
mat2[0][1] = 9

print(mat2)