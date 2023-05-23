import math

for i in range(1,501):
    x = math.sqrt(i)
    if int(x) ** 2 == i:
        print(i)