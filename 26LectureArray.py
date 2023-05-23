'''from array import *
ar=array('i',[])
n=int(input("Enter Array Size : "))
print("Enter ",n, " Elements one by one : ")
for i in range(n):
    x=int(input())
    ar.append(x)

print(ar)

val=int(input("Enter Value for Search : "))
k=0
for i in ar:
    if i==val:
        print(k)
        break
    k += 1

print()
print("Index of ",val,"is : ",ar.index(val))
'''
'''from array import *
a=array('i',[])
print("Enter 5 Values One by One : ")
for i in range(5):
    x=int(input())
    a.append(x)

print("After Deleting value at index 2 : ")
index=0
for i in a:
    if index==2:
        a.remove(i)
    index+=1

for i in a:
    print(i,end=" ")'''

from array import *
ar=array('i',[34,21,56,78,43])
print("Array Before Reversing : ",ar,end=" ")
print()
l=len(ar)
print("Array After Reversing : ")
for i in range(l-1,-1,-1):
    print(ar[i],end=" ")


