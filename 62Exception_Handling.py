a=5
b=0
try:
    print(a/b)
except Exception as e:
    print("Hey you cannot divide a Number by Zero : ",e)

print()
a=5
b=2
try:
    print(a/b)
except Exception:
    print("Hey you cannot divide a Number by Zero ")

print()
a=5
b=0
try:
    print("Resource Open ")
    print(a/b)
    print("Resourse Close ")
except Exception as e:
    print("Hey you cannot divide a Number by Zero : ",e)

print()
a=5
b=0
try:
    print("Resourse Open ")
    print(a/b)
except Exception as e:
    print("Hey you cannot divide a Number by Zero : ",e)
finally:
    print("Resourse Close")