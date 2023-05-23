from array import *
vals=array('i',[23,7,-5,54,])
print(vals)
print("Array Size :  ",vals.buffer_info())
vals.reverse()
print("Reverse of Array :",vals)
vals.pop(2)
print(" After popping Value from index 2 is : ",vals)
vals.append(12)
print("Array after Appending value : ",vals)
for i in range(4):
    print(vals[i])

print()
for i in range(len(vals)):
    print(vals[i])

print()
for i in vals:
    print(i)


charArray=('u',['e','p','r','h'])
print(charArray)


print("Array Typecode : ",vals.typecode)

newArray=array(vals.typecode,(a for a in vals))
for i in newArray:
    print(i)

print()
newArray=array(vals.typecode,(a*a for a in vals))
for i in newArray:
    print(i)

abc=[2,4,5,6,3,2,1,1]
abc.sort()
print("Array after Sorting : " , abc)

x=int(input("Enter Number "))
fact=1
for i in range(1,x+1):
    fact=fact*i

print(fact)