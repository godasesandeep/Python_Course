arr = [64, 34, 25, 12, 22, 11, 90]

def bubble_sort(arr):

    for j in range(len(arr)-1):

        for i in range(len(arr)-j-1):

            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1], arr[i]
    return arr


print(bubble_sort(arr))  
    