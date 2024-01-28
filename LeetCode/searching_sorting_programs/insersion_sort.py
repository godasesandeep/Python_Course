arr = [12, 11, 13, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 7, 7, 7, 7]
#arr = [11, 12, 13, 5, 6] j=3

for j in range(1,len(arr)):       #j=2
    key=arr[j] 
    swap=False                   #key=13
    for i in range(j-1,-1,-1):    #i=1,0
        if arr[i]>key:            #12>13 F ,11>13 F
            arr[i+1]=arr[i]       #
            p=i
            swap=True
        else:
            break
    if swap:
        arr[p]=key

print(arr)

# the function proceeds to iterate over the array starting from the second element.
# It takes the current element (referred to as the “key”) 
#and compares it with the elements in the sorted portion of the array that precede it.
# If the key is smaller than an element in the sorted portion,
# the function shifts that element to the right, creating space for the key. 
#This process continues until the correct position for the key is found, 
#and it is then inserted in that position.

def insertion_sort(arr):
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
  
# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(arr)