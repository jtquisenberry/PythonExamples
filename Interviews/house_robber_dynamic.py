class Solution:
    def rob(self, nums) -> int:

        if not nums:
            return 0

        table = [0] * (len(nums) + 1)
        table[-1] = 0
        table[-2] = nums[-1]

        for i in range(len(table) - 3, -1, -1):
            table[i] = max(table[i + 2] + nums[i], table[i + 1])

        return table[0]