# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 40

def binary_search(arr,x):
    start,end=0,len(arr)-1
    while(start<=end):
        mid=(start+end)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            end=mid-1
        else:
            start=mid+1
    return -1

print(binary_search(arr,x))