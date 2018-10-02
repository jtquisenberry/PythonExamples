import random

# https://www.interviewcake.com/question/python/shuffle?section=greedy&course=fc1
# An incorrect solution that gives non-uniform random results.
# This method uses:
# A common first idea is to walk through the list and swap each element with a random other element.
# The correct solution swaps each element with a random later (or current) element.


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

def naive_shuffle(the_list):
    # For each index in the list
    for first_index in range(0, len(the_list) - 1):
        # Grab a random other index
        second_index = get_random(0, len(the_list) - 1)
        # And swap the values
        if second_index != first_index:
            the_list[first_index], the_list[second_index] = \
                the_list[second_index], the_list[first_index]


results = dict()
for i in range(100000):
    a = [1,2,3]
    naive_shuffle(a)
    if str(a) in results:
        results[str(a)] += 1
    else:
        results[str(a)] = 1

print(results)
# {'[1, 2, 3]': 22206, '[2, 3, 1]': 22143, '[3, 2, 1]': 11124, '[2, 1, 3]': 22449, '[3, 1, 2]': 11099, '[1, 3, 2]': 10979}
# Not even close to uniform

for k,v in sorted(results.items(), key=lambda x: x[1]):
    print(k,v)


#print(list(results).sort(key=lambda x: x[1]))

