import numpy as np

a=np.ones((5,5))
print(a)

b=np.zeros((3,3))
print(b)

b[1,1]=9
print(b)

a[1:4,1:4]=b
print(a)