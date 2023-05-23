class student:
    school="Udemy"
    def __init__(self,n1,n2,n3):
        self.n1=n1
        self.n2=n2
        self.n3=n3

    def avg(self):
        return (self.n1+self.n2+self.n3)/3

    @classmethod
    def info(cls):
        return cls.school

    @staticmethod
    def abc():
        print("This is Static Method")


s1=student(1,2,3)
s2=student(4,5,6)

print(s1.avg())
print(student.info())
print(s2.avg())
print(student.info())
print(s1.abc())
