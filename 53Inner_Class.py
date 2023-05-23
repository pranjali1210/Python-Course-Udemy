class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap1=self.laptop()


    def show(self):
        print(self.name,self.roll)

    class laptop:
        def __init__(self):
            self.brand="HP"
            self.cpu="1TB"
            self.ram="16GB"

s1=student("Pranjali",22)
s2=student("Asha",40)
s1.show()
s2.show()

lap1=s1.lap1.brand
lap2=s2.lap1.cpu

print(lap1)
print(lap2)