from numpy import *
n1=array([
    [1,2,3],
    [4,5,6]
])
print(n1)
print()

print(n1.dtype)
print()

print(n1.ndim)
print()

print(n1.shape)
print()

print(n1.size)
print()

OneDArray=n1.flatten()
print(OneDArray)

ThreeDArr=OneDArray.reshape(3,2)
print(ThreeDArr)

TwoDArr=ThreeDArr.reshape(2,3)
print(TwoDArr)

m=matrix(n1)
print(m)

print()
m1=matrix('1 2 3; 4 5 6; 7 8 9')
print(m1)

print()
print(diagonal(m1))

print()
print(m1.max())

print()
print(m1.min())

print()
mat1=matrix('1 2 3; 4 5 6; 7 8 9')
mat2=matrix('1 2 3; 4 5 6; 7 8 9')
mat3=mat1+mat2
print(mat3)

print()
mat4=mat1*mat2
print(mat4)










