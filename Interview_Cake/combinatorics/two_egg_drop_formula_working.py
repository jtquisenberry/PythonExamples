import unittest
import math

#######################
# Problem
#######################

# A building has 100 floors. One of the floors is the highest floor an egg can be
# dropped from without breaking.

# If an egg is dropped from above that floor, it will break. If it is dropped from
# that floor or below, it will be completely undamaged and you can drop the egg again.

# Given two eggs, find the highest floor an egg can be dropped from without breaking,
# with as few drops as possible.

# Gotchas

# We can do better than a binary approach, which would have a worst case of 50 drops.

# We can even do better than 19 drops!

# We can always find the highest floor an egg can be dropped from with a worst case
# of 14 total drops.

#######################
# Discussion
#######################

# Binary is out of the question because we have only two eggs. We could drop on floor 50 and
# then on floor 25. If the egg breaks both times, we do not have a solution.

# Can do a part divide and conquer and part linear. Within each chunk, say, 10 floors, we must
# test every floor from lowest to highest. Otherwise, we risk breaking an egg without narrowing
# down which floor is the highest safe floor.

# If we divide 100 into chunks of 10 and assume the worst case (floor 99), we drop at
# Round  1: egg1 at floor  10, survives
# Round  2: egg1 at floor  20, survives
# ...
# Round 10: egg1 at floor 100, breaks; egg2 at 91..99
# = 19 drops.
# However, if the highest safe floor = 9, we only drop at
# Round  1: egg1 at floor 10, breaks; egg2 at 1..9
# That is only 10 drops.

# To minimize the number of drops in the worst case we want to make the number of drops constant
# for all cases.

# Instead of fixed-size chunks, reduce the size of the chunk each round to reflect the fact that
# testing the previous chunk took up one drop.
# x + (x-1) + (x-2) + x-3 + ... + 1 >= 100
# Simplifies to x(x+1) / 2


def get_egg_drops_given_floors(floors=0):


    # Reduce the number of floors skipped with the first egg by one each time the first egg does
    # not break. This is because we want the number of drops of both eggs to remain constant.

    # Round  1: egg1 = 1st drop at floor 14. egg2 13 drops (1 - 13) = 14 drops
    # Round  2: egg1 = 2nd drop at floor 27, egg2 12 drops (15 - 26) = 14 drops
    # Round  3: egg1 = 3rd drop at floor 39, egg2 11 drops (28 - 38) = 14 drops
    # ...
    # Round 11: egg1 = 11th drop at floor 99, egg2 3 drops (96 - 98) = 14 drops
    # Round 12: egg1 = 1

    # Using the quadratic formula
    answer1 = (-1 + math.sqrt(1 ** 2 - 4 * 1 * (-2 * floors))) / (2 * 1)
    answer1 = int(answer1) if answer1 % 1 == 0 else int(answer1) + 1
    answer2 = (-1 - math.sqrt(1 ** 2 - 4 * 1 * (-2 * floors))) / (2 * 1)
    answer2 = int(answer2) if answer2 % 1 == 0 else int(answer2) + 1

    return max(answer1, answer2)


class Test(unittest.TestCase):

    def test_floor_100(self):
        # expected = 13.650971698084906
        expected = 14
        actual = get_egg_drops_given_floors(100)
        self.assertEqual(expected, actual)

    def test_floor_753(self):
        expected = 39
        actual = get_egg_drops_given_floors(753)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
