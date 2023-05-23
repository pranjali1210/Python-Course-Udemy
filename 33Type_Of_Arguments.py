def add(x,y):
    c=x+y
    print(c)

add(4,3)

print()
def person(name,age):
    print(name)
    print(age)

person(name='Pranjali',age=22)

print()
def person(name,age=22):
    print(name)
    print(age)

person('Asha')

print()
def sum(a,*b):
    c=a
    for i in b:
        c=c+i

    print(c)

sum(3,4,5,1,2)