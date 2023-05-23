class car():
    wheels=5
    def __init__(self):
        self.mil=10
        self.name="BMW"

c1=car()
c2=car()

c1.mil=15

print(c1.mil, c1.name, c1.wheels)
print(c2.mil, c2.name, c2.wheels)