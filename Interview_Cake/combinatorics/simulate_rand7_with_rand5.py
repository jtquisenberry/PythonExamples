import random


# https://www.interviewcake.com/question/python/simulate-7-sided-die?course=fc1&section=combinatorics-probability-math
# Simulate seven-sided die with five-sided die
# Use a five-sided die to create a range possibilities > 7 (5 * 5 = 25)
# Remove results after the last position divisible by 7 (the last index -1 divisible by 7)
# Reroll whenever 21-24 is rolled.
# Time = O(n)
# Space = O(1)


def rand5():
    return random.randint(1, 5)


def rand7():
    # Implement rand7() using rand5()

    # represent the outcome as a sequence from 0 to possibilities -1
    which_outcome = float('inf')

    while which_outcome > 21:
        # The number of possible outcomes is 5 * 5 = 25.
        roll1 = rand5()
        roll2 = rand5()

        which_outcome = (roll1 - 1) * 5 + (roll2 - 1) + 1
        # print('which_outcome', which_outcome)

    result = which_outcome % 7 + 1
    # print('result', result)

    return result


print('Rolling 7-sided die...')
print(rand7())

results = {}
for i in range(100000):
    result = rand7()
    if result in results:
        results[result] += 1
    else:
        results[result] = 1

print(results)

results = list(results.items())
results.sort(key=lambda x: x[1])
print(results)

# [(4, 14149), (7, 14154), (6, 14259), (1, 14262), (2, 14355), (5, 14392), (3, 14429)]