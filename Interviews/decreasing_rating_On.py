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
    interim_count = 0
    total_count = 0

    print(ratings)
    previous_number = -1
    for i in range(len(ratings)):
        if ratings[i] == previous_number - 1:
            interim_count += 1
            previous_number = ratings[i]

        else:
            print(interim_count)
            total_count += (interim_count ** 2 + interim_count) / 2
            interim_count = 1

            previous_number = ratings[i]
            b = 1
    print(interim_count)
    total_count += (interim_count ** 2 + interim_count) / 2
    return int(total_count)


ratings = [x for x in range(200, 0, -1)]
ratings.extend([x for x in range(10, 0, -1)])
ratings.extend([x for x in range(20, 0, -1)])
print(ratings)
#ratings = [3, 2, 1, 3]
print("Total:", countDecreasingRatings(ratings))
