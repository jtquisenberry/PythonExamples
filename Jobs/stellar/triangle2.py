#https://leetcode.com/problems/triangle/

from copy import deepcopy


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]


def minimumTotal(triangle):
    print(triangle)
    #triangle2 = triangle.copy()  # updates triangle and triangle2
    #triangle2 = list(triangle)  # updates triangle and triangle2
    #triangle2 = triangle[:]  # updates triangle and triangle2
    triangle2 = deepcopy(triangle)  # updates triangle only
    triangle2[0][0] = 99
    print(triangle)
    print(triangle2)


if __name__ == '__main__':
    minimumTotal(triangle=triangle)
