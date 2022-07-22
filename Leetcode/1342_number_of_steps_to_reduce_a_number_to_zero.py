from typing import *


class Solution:
    def numberOfSteps(self, num: int) -> int:

        steps = 0

        while num > 0:
            # print(num, bin(num))
            if num & 1:
                steps += 1
            steps += 1
            num = num >> 1
            # print(steps)

        if steps - 1 > -1:
            return steps - 1
        return 0

# Input
#14
#8
#123



# Output
#6
#4
#12
