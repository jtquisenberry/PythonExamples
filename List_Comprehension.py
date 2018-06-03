# Find the proportion of combinations containing
# the letter 'a'.

from itertools import combinations
#import itertools

#n = input()
#letters = input().strip().split(' ')
letters = ['a', 'a', 'b', 'c']
#number = int(input())
number = 2

letter_combinations = (list(combinations(letters, number)))
denominator = len(letter_combinations)
numerator = sum([1 for z in letter_combinations if 'a' in z])
print(numerator / denominator)
