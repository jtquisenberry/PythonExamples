from sklearn.manifold import TSNE
import numpy as np

arr1 = [1,1,3,4,5,1]
v = np.array(arr1)
print(v)

tsne = TSNE(n_components=1)
v  = np.array.res
a = tsne.fit_transform(v.reshape(-1))
print(a)