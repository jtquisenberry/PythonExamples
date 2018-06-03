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


'''
http://www.pythonforbeginners.com/basics/list-comprehensions-in-python
new_list    
The new list (result).

expression(i)
Expression is based on the variable used for each element in the old list.

for i in old_list
The word for followed by the variable name to use, followed by the word in the
old list.

if filter(i)
Apply a filter with an If-statement.
This blog shows an example of how to visually break down the list comprehension:

new_range  = [i * i          for i in range(5)   if i % 2 == 0]

Which corresponds to:

*result*  = [*transform*    *iteration*         *filter*     ]

The * operator is used to repeat. The filter part answers the question if the
item should be transformed. 
'''
