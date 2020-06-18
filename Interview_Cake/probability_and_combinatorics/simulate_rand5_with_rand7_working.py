import random


# https://www.interviewcake.com/question/python/simulate-5-sided-die?section=combinatorics-probability-math&course=fc1
# Simulate a five-sided die with a seven-sided die
# Reroll the die any time a number > 5 is rolled.
# Use iteration, rather than recursion to avoid infinite space on the call stack.
# Time = O(infinite)
# Space = O(1)

def rand7():
    return random.randint(1, 7)


def rand5():
    # Implement rand5() using rand7()
    selected_number = 999
    while selected_number > 5:
        selected_number = rand7()

    return selected_number

print('Rolling 5-sided die...')
print
rand5()

# Check randomness
if __name__ == '__main__':
    results = dict()
    results = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

    for i in range(100000):
        result = rand5()
        results[result] += 1

    results = list(results.items())
    results.sort(key=lambda x: x[0])
    print(results)

# [(5, 19829), (1, 19994), (3, 20039), (2, 20052), (4, 20086)]
