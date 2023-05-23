import sys
sys.setrecursionlimit(50)
print(sys.getrecursionlimit())
def greet():
    print("Hello")
    greet()

greet()