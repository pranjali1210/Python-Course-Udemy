pos=-1
def BinarySearch(list,n):
    l = 0
    u = len(list) - 1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals() ['pos']=mid
            return  True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return  False

list=[4,5,34,65,251,999]
n=int(input("Enter Element to Search : "))
if BinarySearch(list,n):
    print("Element found at : ",pos+1)
else:
    print("Element Not Found .")