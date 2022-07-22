from functools import lru_cache

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

class Solution:
    def minimumTotal(self, triangle):
        @lru_cache()
        def dfs(i, level):
            if level == len(triangle):
                return 0

            left = triangle[level][i] + dfs(i, level + 1)
            right = triangle[level][i] + dfs(i + 1, level + 1)

            return min(left, right)

        return dfs(0, 0)

solution = Solution()
print(solution.minimumTotal(triangle))
