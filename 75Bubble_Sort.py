def sort(list):
    for i in range(0,len(list)-1,1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp

list=[3,9,1,6,7,2]
sort(list)
print(list)