
arr = [64, 34, 25, 12, 12, 22, 11, 90, 1]

for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]= arr[j],arr[i]  # insted of doing swapping to every element we found first 
                                          # we find minimum element and then @ end we swap it please find below code

print(arr)

arr1 = [64, 34, 25, 12, 12, 22, 11, 90, 1, 2, 4, 0]

def selection_sort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort(arr1))

# To find the minimum index position 

arr1 = [64, 34, 25, 12, 12, 22, 11, 90, 1, 2, 4]
min_element_index=0
for i in range(1,len(arr1)):
    if arr1[min_element_index] > arr1[i]:
        min_element_index=i

print("minimum element is @ index : " , min_element_index)






