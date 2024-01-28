#Find largest element in an array Using Native Approach

arr = [10, 324, 45, 90, 9808, 100]

def largest_element(arr):
    n=len(arr)
    max=arr[0]
    for i in range(n):
        if arr[i]>max:
            max=arr[i]
    return max

print(largest_element(arr))

#Find largest element in an array Using built-in function max()
print(max(arr))

#Find largest element in an array Using sort() function
arr.sort()
print(arr[-1])

#Find largest element in an array Using reduce() function

from functools import reduce
arr = [10, 324, 45, 90, 9808, 100]
print(reduce(max,arr))
