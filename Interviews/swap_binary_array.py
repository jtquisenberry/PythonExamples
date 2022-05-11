# Given an array of 0s and 1s, find the minimum number of swaps to sort
# either the 0s to the beginning or the 1s to the beginning.
# For each 0 to the right of a 1, the 1 must be swapped once.
# In [0, 1, 0, 0], it takes two moves to shift the 1 all the way
# to the right. In [1, 0, 1, 0, 0], it takes two moves to move the
# last move all the way to the right, plus three moves to move the
# first one all the way to the right.

def minMoves(arr):
    # Write your code here

    result_0 = 0
    result_1 = 0

    number_of_unsorted_zeros = 0
    number_of_unsorted_ones = 0

    number_of_swaps_0 = 0
    number_of_swaps_1 = 1

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 0:
            number_of_unsorted_zeros += 1
            result_1 += number_of_unsorted_ones
        else:  # 1s
            result_0 += number_of_unsorted_zeros
            number_of_unsorted_ones += 1

    print(result_0, result_1)
    # print(min(result_0, result_1))
    return min(result_0, result_1)


arr = [1, 0, 1, 0, 0]
print(minMoves(arr))