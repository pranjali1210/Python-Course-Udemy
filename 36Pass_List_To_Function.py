def count(lst):
    evenC=0
    oddC=0
    for i in lst:
        if i%2==0:
            evenC+=1
        else:
            oddC+=1

    return  evenC,oddC

lst=[]
n=int(input("Enter Size : "))
for i in range(n):
    x=int(input("Enter Element : "))
    lst.append(x)

e1,o1=count(lst)
print("Total Even : ",e1)
print("Total Odd : ",o1)
print("Even : {} and Odd : {}".format(e1,o1))
