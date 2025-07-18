import numpy as np 
array=np.array([10,20,30])
print(array+2)
print(array*2)
print(array**2)

#aggregration function 
#  function        what it does -
#  np.sum(array)   adds all elements 
#  np.mean(array)  average 
#  np.min(array)   min
#  np.max(array)   max
#  np.std(array)   std deviation
#  np.var(array)   variance

array=np.array([1,2,3,4])
print(np.sum(array))
print(np.mean(array))
print(np.min(array))   
print(np.max(array))
print(np.std(array))    
print(np.var(array))

#INDEXING(0 based indexing) 
#TO ACCESS A SPECIFIC POSITION OR ELEMENT 
array=np.array([1,2,3,4,5,6])
print(array[2])
print(array[-5])

#SLICING (accessing subset of data from parent array)
#(START, STOP, STEP)
#Indexing number gets excluded
array=np.array([1,2,3,4,5,6])
print(array[2:4])
print(array[:4])
print(array[3:])
print(array[::3])
print(array[-2])

#Fancy indexing (selection multiple elements at once/to extract a part of sequence like a list array or string)
array=np.array([1,2,3,4,5,6])
print(array[[0,2,4]])

#Filtering 
array=np.array([1,2,3,4,5,6])
print(array[array>3])

