def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)

person('Pranjali',age=22,City='Pune',Mob=8746599342)