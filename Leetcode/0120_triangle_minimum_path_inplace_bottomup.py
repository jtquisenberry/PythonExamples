#https://leetcode.com/problems/triangle/solution/

# Time Complexity: O(n^2)
# Space Complexity: O(n)

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

def minimumTotal(triangle):
    # print(triangle)
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += min(triangle[row+1][col], triangle[row+1][col+1])

    # print(triangle)
    return triangle[0][0]

result = minimumTotal(triangle=triangle)
print(result)

# Expected = 11