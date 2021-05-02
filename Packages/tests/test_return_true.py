import sys
print(sys.path)
from Packages.Functions.return_true import return_true

import unittest

class Test(unittest.TestCase):
    def test_true(self):
        self.assertEqual(True, return_true())