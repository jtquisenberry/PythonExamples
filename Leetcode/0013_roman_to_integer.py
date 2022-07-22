#https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:

        conversions = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        result = 0
        for idx, c in enumerate(s):
            current_number = conversions[c]

            if idx + 1 == len(s):
                result += current_number
            else:
                next_number = conversions[s[idx + 1]]
                if next_number > current_number:
                    result -= current_number
                else:
                    result += current_number

        return result



