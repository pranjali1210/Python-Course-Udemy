a=10
def something():
    a=15
    print("In side : ",a)

something()
print("Out side : ",a)

print()
a=10
def something():
    global a
    a=15
    print("In side : ",a)

something()
print("Out side : ",a)

print()
a=10
print(id(a))
def something():
    a=9
    x=globals()['a']
    print(id(x))
    globals()['a']=15
    print("In side : ",a)

something()
print("Out side : ",a)