#Reshaping-Changing the shape (rows, columns, dimensions) of an array without changing its data.
#MODIFYING-Changing the actual values or structure of an array — like updating, adding, or removing elements.

#reshape- if dimensions match - reshaping does not create copy 

import numpy as np 
array = np.array([1,2,3,4,5,6,7,8,])
reshaped_array=array.reshape(2,4)
print(reshaped_array)

#flatning arrays - types- ravel(view) and flatten(returns a copy)
array = np.array([[1,2,3,4],[5,6,7,8]])
print(array.ravel())
print(array.flatten())
array.flatten()[0]=100
array.ravel()[1]=200
print(array.ravel())
print(array.flatten())