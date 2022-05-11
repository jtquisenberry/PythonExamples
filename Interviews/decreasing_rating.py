# A day range is decreasing if and only if it consists of
# r, r-1, r-2, ... ratings
# The pattern [3, 2, 1, 3] consists of the following decreasing ranges:
# [3], [2], [1], [3], [3, 2], [3, 2, 1], [2, 1]
# That is 7 values

# WARNING: For large inputs, this is too slow (> 10 seconds)
# WARNING: This does not address edge cases.
# It could be sped up from O(n^2) to O(n) by advancing the outer loop when non-decreasing
# ranges are found.

def countDecreasingRatings(ratings):
    # Write your code here
    count = 0

    print(ratings)
    for i in range(len(ratings)):
        j = 0
        while i + j < len(ratings):
            if i-i-j == ratings[i+j] - ratings[i]:
                count += 1
                print(ratings[i], ratings[i + j], i - i - j == ratings[i + j] - ratings[i], count)

            else:
                print(ratings[i], ratings[i + j], i - i - j == ratings[i + j] - ratings[i], count)
                break
            j += 1
    return count


ratings = [3, 2, 1, 3]
countDecreasingRatings(ratings)
