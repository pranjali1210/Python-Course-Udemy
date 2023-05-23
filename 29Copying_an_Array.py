'''from numpy import *
arr=array([1,2,3,4,5])
arr=arr+5

print(arr)

arr1=array([1,2,3,4,5])
arr2=arr+arr1
print(arr2)

print(sin(arr1))
print()
print(cos(arr1))
print()
print(sqrt(arr1))
print()
print(sum(arr1))
print()
print(min(arr1))
print()
print(max(arr1))
print()
print(concatenate([arr,arr1]))
print()

n1=array([1,2,3,4,5])
n2=n1
print(n1)
print(n2)
print()
print(id(n1))
print(id(n2))
print()

n2=n1.view()
print(id(n1))
print(id(n2))

n2=n1.copy()
print(n1)
n2[1]=7
print(n2)
print(id(n1))
print(id(n2))'''

'''from numpy import *
n1=array([1,2,3,4,5])
n2=array([6,7,8,9,10])
for i in n2:
    n1=n1+n2
    print(n1)
    break
'''

from numpy import *
n1=array([23,459,21,9,76])
x=n1[0]
for i in range(1,len(n1)):
    if n1[i]>x:
        x=n1[i]

print(x)

