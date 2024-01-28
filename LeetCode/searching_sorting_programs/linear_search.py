#leanear search
#Example
#Input : arr[] = {10, 20, 80, 30, 60, 50, 110, 100, 130, 170}
# x = 110;
#Output : 6
#Element x is present at index 6

arr =[10, 20, 80, 30, 60, 50, 110, 100, 130, 170]

def linear_search(arr,element):
    count=0
    for i in arr:
        count +=1
        if i==element:
            print("Element is present at index : ", count-1)
            break
    else:
        print("Element not present ")
    

linear_search(arr,100)

# If you want to implement Linear Search in python
 
# Linearly search x in arr[]
# If x is present then return its location
# else return -1

def search(arr, x):
 
    for i in range(len(arr)):
 
        if arr[i] == x:
            return i
 
    return -1

print(search(arr,100))