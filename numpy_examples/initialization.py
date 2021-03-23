import numpy as np
import math
import random

random.seed(8472)
np.random.seed(8472)

print("ZEROS")
A = np.zeros((3, 2), dtype=np.int)
print(A)
print()

print("ONES")
A = np.ones((3, 2))
print(A)
print()

print("GAUSSIAN")
A = np.random.randn(3, 2)
print(A)
print()

print("RANDOM INTEGERS")
A = np.random.randint(4, 55, (3, 2), dtype=np.int)
print(A)
print()



