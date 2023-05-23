class computer:
    def __init__(self):
        self.name="Pranjali"
        self.age=22

    def update(self):
        self.age=30

    def compare(self,c2):
        if self.age==c2.age:
            return  True
        else:
            return False

c1=computer()
c2=computer()
c1.name="Asha"
c1.update()
if c1.compare(c2):
    print("They are Same")
else:
    print("They are Different")

print(c1.age)
print(c2.age)
print(c1.name)
print(c2.name)