import random
random.seed(8472)

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

    total = 999
    while total > 21:

        # Treat each roll as a digit in a base-5 number
        # Subtract 1 from each roll so that zero is a possible result.
        # Add 1 to total to produce a number in range 1..25
        roll1 = rand5()
        roll2 = rand5()
        total = 5 * (roll1 - 1) + 1 * (roll2 - 1) + 1
        retval = total % 7

    return retval


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
results.sort(key=lambda x: x[0])
print(results)

# [(1, 14214), (2, 14334), (3, 14194), (4, 14440), (5, 14301), (6, 14352), (7, 14165)]