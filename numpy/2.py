import numpy as np

a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
# print(a)

# #GEt a specific element
# print(a[1,5])
# #Get a specific row
# print(a[0, :])
# #get a specific column
# print(a[:, 2])

# print(a[0,1:6:2])

# #change
# a[0,3]=20
# print(a)

# a[:,2]=55
# print(a)

b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

print(b[0,1,1])