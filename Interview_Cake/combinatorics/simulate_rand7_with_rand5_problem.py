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
    """
    Implement rand7() using rand5()

    Add code below.
    """




    return result


print(rand7.__doc__)
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