#https://leetcode.com/problems/triangle/solution/

from functools import lru_cache


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
sums = []


def minimumTotal(triangle):
    # print(triangle)
    return dfs(0, 0)


@lru_cache()
def dfs(row_index, col_index):

    if row_index == len(triangle):
        return 0

    left_triangle = triangle[row_index][col_index] + dfs(row_index + 1, col_index)
    right_triangle = triangle[row_index][col_index] + dfs(row_index + 1, col_index + 1)
    # print(row_index, col_index, left_triangle, right_triangle)
    return min(left_triangle, right_triangle)


result = minimumTotal(triangle=triangle)
print(result)

# Expected = 11
