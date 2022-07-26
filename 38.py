
# Python program to multiply two matrices

import numpy as np 

mat1=np.array([[10,20,30],[40,50,60],[70,80,90]])
mat2=np.array([[1,2,3],[4,5,6],[7,8,9]])

print(mat1*mat2)

print(np.dot(mat1,mat2))

