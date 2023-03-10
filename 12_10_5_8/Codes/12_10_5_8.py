import numpy as np
from numpy import linalg as LA

#Given points
A = np.array(([1,-2,-8]))
B = np.array(([5,0,-2]))
C = np.array(([11,3,7]))

#Calculating AB and AC

AB = np.subtract(A,B)
AC = np.subtract(A,C)

#Form the matrix with transposes of A,B,C
mat = np.block([[AB],[AC]])

rankOfMatrix = LA.matrix_rank(mat)

if(rankOfMatrix == 1):
    print("The rank of the  matrix is ", rankOfMatrix, ". Hence the points are collinear")
else:
    print("The rank of the matrix is ", rankOfMatrix, ". Hence the points are not collinear")


# Calculating ratio in which B divides AC
# k = (A-B)/(B-C)

BC = np.subtract(B,C)
k = (AB/BC)[0]
print("Ratio in which B divides AC is ", k)
