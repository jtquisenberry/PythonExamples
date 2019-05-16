import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a DataFrame based on a dictionary.
d = {'timeIndex': [1, 1, 1, 1, 1, 1, 1, 2, 2, 2], 'isZero': [0,0,0,1, 1, 1, 1 ,0,1,0],
     'isOne':[99,98,99,88,78,89,96,99,97,93], 'xTimes':[0,1,2,3,4,5,6,7,8,9]}
df = pd.DataFrame(data=d)

my_array = df.values
print(my_array)

my_matrix = np.asmatrix(my_array)
print(type(my_matrix))
print(my_matrix)

a = 1