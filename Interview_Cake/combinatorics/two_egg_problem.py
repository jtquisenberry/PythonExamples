import unittest
import math

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


def get_egg_drops_given_floors(floors = 0):


    # Reduce the number of floors skipped with the first egg by one each time the first egg does
    # not break. This is because we want the number of drops of both eggs to remain constant.

    # Round  1: egg1 = 1st drop at floor 14. egg2 13 drops (1 - 13) = 14 drops
    # Round  2: egg1 = 2nd drop at floor 27, egg2 12 drops (15 - 26) = 14 drops
    # Round  3: egg1 = 3rd drop at floor 39, egg2 11 drops (28 - 38) = 14 drops
    # ...
    # Round 11: egg1 = 11th drop at floor 99, egg2 3 drops (96 - 98) = 14 drops
    # Round 12: egg1 = 1

    answer1 = (-1 + math.sqrt(1 ** 2 - 4 * 1 * (-2 * floors))) / (2 * 1)
    answer2 = (-1 - math.sqrt(1 ** 2 - 4 * 1 * (-2 * floors))) / (2 * 1)

    return answer1



class Test(unittest.TestCase):

    def test_floor_100(self):
        expected = 13.650971698084906
        actual = get_egg_drops_given_floors(100)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()