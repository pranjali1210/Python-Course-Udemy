def greet():
    print("Hello")
    print("Welcome In Python !!")

greet()

print()

def add(x,y):
    c=x+y
    print(c)

add(3,2)

print()
def add(x,y):
    c=x+y
    return c

result=add(5,4)
print(result)

print()
def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

r1,r2=add_sub(5,3)
print(r1)
print(r2)