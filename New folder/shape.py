# 1)shape- to check the rows and columns 
import numpy as np 
array_2d=np.array([[1,2,3],
                   [4,5,6]])
print(array_2d.shape)

# 2)size- to check the total number of elements 
array_size=np.array([[1,2,3],[4,5,6]])
print(array_size.size)

# 3)NDIM - number of dimensions 
array_1dimension=np.array([9,0,6])
array_2dimension=np.array([[1,2],[4,5],[9,0]])
array_3dimension=np.array([[[1,2,3],[4,5,6],[9,0,6]]])
print(array_1dimension.ndim)
print(array_2dimension.ndim)
print(array_3dimension.ndim)

# 4).dtype- data tyoe of elements (int, float...)
array_dtype=np.array([12,3,56,59])
print(array_dtype.dtype)


#TO CHANGE THE DATA TYPE OF A VARIABLE 
# To covert the float values to int 
array_3=np.array([2.4,3.6,4.7])
int_array_3=array_3.astype(int)
print(int_array_3)
print(int_array_3.dtype)

#float to int 
folatarr=np.array([1,2,3])
float_floatarr=folatarr.astype(float)
print(float_floatarr)
print(float_floatarr.dtype)
