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

# As discussed in `two_egg_drop_formula_working.py`, we want to reduce the size of chunks
# of floors for each round to reflect the fact that testing a chunk uses up one drop.
# Instead of a formula, here is a bottom-up approach.
# Assume that we will test one floor in the final round, two floors in the previous round,
# three floors in the round before that, and so on.


def get_egg_drops_given_floors(floors=0):

    cumulative_drops = 0
    amount_to_add = 0
    while cumulative_drops < floors:
        amount_to_add += 1
        cumulative_drops += amount_to_add

    return amount_to_add


class Test(unittest.TestCase):

    def test_floor_100(self):
        expected = 14
        actual = get_egg_drops_given_floors(100)
        self.assertEqual(expected, actual)

    def test_floor_753(self):
        expected = 39
        actual = get_egg_drops_given_floors(753)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()