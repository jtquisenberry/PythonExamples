# https://leetcode.com/problems/fizz-buzz/submissions/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        results = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                results.append("FizzBuzz")
            elif i % 5 == 0:
                results.append("Buzz")
            elif i % 3 == 0:
                results.append("Fizz")
            else:
                results.append(str(i))

        return results
