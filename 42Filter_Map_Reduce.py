
from functools import reduce
lst=[2,9,4,5,6,]
even=list(filter(lambda n:n%2==0,lst))
print(even)

doubles=list(map(lambda n:n*2,even))
print(doubles)

sum=reduce(lambda a,b:a+b,doubles)
print(sum)