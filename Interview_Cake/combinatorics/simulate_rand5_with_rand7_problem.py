import random

#######################
# Problem
#######################

# You have a function rand7() that generates a random integer from 1 to 7.
# Use it to write a function rand5() that generates a random integer from 1 to 5.

# rand7() returns each integer with equal probability. rand5() must also return each
# integer with equal probability.


# https://www.interviewcake.com/question/python/simulate-5-sided-die?section=combinatorics-probability-math&course=fc1
# Simulate a five-sided die with a seven-sided die
# Reroll the die any time a number > 5 is rolled.
# Use iteration, rather than recursion to avoid infinite space on the call stack.
# Time = O(infinite)
# Space = O(1)

def rand7():
    return random.randint(1, 7)


def rand5():

    return result


print('Rolling 5-sided die...')
print
rand5()

# Check randomness

results = dict()
for i in range(100000):
    result = rand5()
    if result in results:
        results[result] += 1
    else:
        results[result] = 1

results = list(results.items())
results.sort(key=lambda x: x[1])
print(results)

# [(5, 19829), (1, 19994), (3, 20039), (2, 20052), (4, 20086)]
