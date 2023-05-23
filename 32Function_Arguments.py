def update(lst):
    lst[1]=46
    print(id(lst))
    print(lst)

lst=[10,20,30]
print(id(lst))
update(lst)
print(lst)