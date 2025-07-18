#INSERTING 
#1d
import numpy as np 
array=np.array([1,2,4])
array1d=np.insert(array,2,[3],axis=0)
print(array1d)

#2d
array2=np.array([[1,3],[2,4]])
print(array)
array2d=np.insert(array2,2,[5,6],axis=1)
print(array2d)

#3d
#Inserting at axis=0 → insert a block of shape (3, 4)
#Inserting at axis=1 → insert a row of length 4 inside each block
#Inserting at axis=2 → insert a column of length 3 inside each row of each block
array3=np.array([[[1,2,3],[7,8,9],[10,11,12]]])
print(array3)
array3d=np.insert(array3,1,[[4,5,6]],axis=2)
print(array3d)

#append (adding element at the end)
array=np.array([1,2,3,4])
array1=np.append(array,[5,6,7,8])
print(array1)

#concatination (joining two arrays)
array1=np.array([1,2,3])
array2=np.array([7,8,9])
array12=np.concatenate((array1,array2))
print(array12)
#axis 0 is vertical stacking 
#axis 1 is horizontal stacking 
array12=np.concatenate((array1,array2),axis=0)
print(array12)

#