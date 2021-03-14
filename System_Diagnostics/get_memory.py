import psutil
import sys
import os
import numpy as np
import cython
from guppy import hpy

#X = np.random.randn(300000,400000,300000)

X = np.random.randn(2,3,4)

h = hpy()

x = psutil.virtual_memory()

psutil.swap_memory()

print(x)