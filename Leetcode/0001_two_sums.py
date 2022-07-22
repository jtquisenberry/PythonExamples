from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = dict()

        for idx, num in enumerate(nums):
            if (target - num) in n:
                return [n[target - num], idx]
            n[num] = idx
        return [0, 0]
