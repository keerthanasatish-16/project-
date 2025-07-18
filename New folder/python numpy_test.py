python_list = [1,2,3,4,5]
print(python_list)

import numpy as np
numpy_array=np.array([1,2,3,4,5])
print(numpy_array)

#1d array 
array_1d=np.array([10,20,30,40])
print(array_1d)

#2d array
array_2d = np.array([[30,40,50,60],   
                     [23,90,80,56],
                     [23,67,34,56]])
print(array_2d)

#multi-dimensional array 
#matrix 
matrix=np.array([[1,2,3,4,],
                 [3,4,5,6]])
print(matrix)

#creating arrays from python list
import numpy as np 
array=np.array([1,3,4,5])
print(array)

#with default values 
import numpy as np 
zero_array=np.zeros(3)
print(zero_array)

#to create a table 
table=np.ones((2,5))
print(table)

#full function - it tell us how big n what number should be put everywhere 
farray=np.full((2,2),7)
print(farray)

#sequences of numbers in numpy 
#arange function(start,stop,step)
#so it starts counts from 1 and stops before 10 n how big are the steps
arr=np.arange(1,10,2)
print(arr)

#creating identity matrices
# have equaly row and columns n diagonal elements are 1 rest 0
identity_matrix=np.eye(4)
print(identity_matrix)


