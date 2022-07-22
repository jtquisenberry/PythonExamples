#https://leetcode.com/problems/triangle/solution/

# Time Complexity: O(n^2)
# Space Complexity: O(n)

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

def minimumTotal(triangle):
    # print(triangle)
    for row in range(len(triangle)):
        for col in range(len(triangle[row])):
            if row == 0:
                continue
            if col == 0:
                triangle[row][col] += triangle[row - 1][0]
            elif col == len(triangle[row]) - 1:
                triangle[row][col] += triangle[row - 1][len(triangle[row - 1]) - 1]
            else:
                # middle element
                triangle[row][col] += min(triangle[row - 1][col - 1], triangle[row - 1][col])

    # print(triangle)
    return min(triangle[len(triangle) - 1])

result = minimumTotal(triangle=triangle)
print(result)

# Expected = 11