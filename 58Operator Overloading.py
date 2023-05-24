'''a=5
b=4
print(a+b)

print(int.__add__(a,b))

print(int.__mul__(a,b))'''

class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        p1=self.m1+other.m1
        p2=self.m2+other.m2
        s3=student(p1,p2)

        return s3

    def __mul__(self, other):
        r1=self.m1*other.m1
        r2=self.m2*other.m2
        t3=student(r1,r2)
        return  t3

s1=student(1,2)
s2=student(2,4)

s3=s1+s2
t3=s1*s2

print(s3.m1)
print(s3.m2)

print(t3.m1)
print(t3.m2)

