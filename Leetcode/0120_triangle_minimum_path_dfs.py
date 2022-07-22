#https://leetcode.com/problems/triangle/solution/

# Time Complexity: O(n^2)
# Space Complexity: O(n)

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
sums = []

def minimumTotal(triangle):
    # print(triangle)

    results = []
    stack = []
    stack.append([(0, 0), triangle[0][0]])

    while len(stack) > 0:
        coordinates, total = stack.pop()
        row = coordinates[0]
        col = coordinates[1]
        if row + 1 < len(triangle):
            left_triangle = [(row + 1, col),  triangle[row+1][col] + total]
            right_triangle = [(row + 1, col + 1), triangle[row + 1][col + 1] + total]
            stack.append(left_triangle)
            stack.append(right_triangle)
            print(stack)
            x = 1
        else:
            results.append(total)
            y = 1
    result = min(results)
    return result




result = minimumTotal(triangle=triangle)
print(result)

# Expected = 11