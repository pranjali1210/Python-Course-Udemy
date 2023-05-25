f=open('MyData','r')
#print(f.read())

print()
#print(f.readline())

'''print()
f1=open('ABC','a')

for data in f:
    f1.write(data)
'''

f=open('images.jpg','rb')
f1=open('Flower.jpg','wb')
for i in f:
    f1.write(i)
