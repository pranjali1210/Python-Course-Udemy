'''a=0
print(a,end=" ")
b=1
print(b, end=" ")
count=1
for i in range(2,100):

    if count >= 50:
        break

    temp=a+b
    a=b
    b=temp
    print(temp,end=" ")
    count+=1
    i+=1'''

x=int(input("Enter Number "))
count=0

for i in range(1,x+1):
     if x % i == 0:
            count+=1

if count==2:
    print(x," is prime")
else:
    print(x," is Not Prime")

