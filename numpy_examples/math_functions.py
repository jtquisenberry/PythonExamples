import numpy as np
import math
import random

random.seed(8472)
np.random.seed(8472)

print("GAUSSIAN")
A = np.random.randn(2, 3)
print(A)
print()

B = np.abs(A)
print(B)
print()

B = np.mean(A)
print(B)
print()

B = np.mean(A, axis=1)
print(B)
print()

B = np.exp(A)
print(B)
print()