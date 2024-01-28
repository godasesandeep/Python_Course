arr=[5,2,7,8,1,3,4]

def quick_sort(arr,low,high):
    if low<high:
        pivot=partition(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)


def partition(arr,low,high):
    print(arr,low,high)
    pivot=high
    i=low-1
    for j in range(low,high):
        if arr[j]<arr[pivot]:
            i +=1
            print(i,j)
            arr[i],arr[j]=arr[j],arr[i]
            print(arr)

    arr[i+1],arr[pivot]=arr[pivot],arr[i+1]
    return i+1

quick_sort(arr,0,len(arr)-1)

print(arr)