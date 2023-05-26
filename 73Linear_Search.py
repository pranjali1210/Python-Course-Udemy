pos=-1
def search(list,n):
    for i in range(len(list)):
        if list[i]==n:
            globals() ['pos']=i
            return True

    return False

list=[3,5,2,8,6]
n=int(input("Enter Key Element to Search : "))

if search(list,n):
    print("Element Found At Index : ",pos+1)
else:
    print("Element Not Found ")