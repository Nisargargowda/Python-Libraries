import numpy as np

a=np.array([1,2,3], dtype='int16')
print(a)

b=np.array([[1.0,2.0],[3.0,4.0]])
print(b)

print(a.ndim)

print(b.ndim)

#get Shape
print(a.shape)
print(b.shape)

print(a.dtype)
print(b.dtype)

print(a.itemsize)

#GEt total size
print(a.size)

print(a.nbytes)

