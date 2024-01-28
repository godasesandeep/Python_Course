
#An array is monotonic if it is either monotone increasing or monotone decreasing.
#Note: Array with single element can be considered to be both monotonic increasing or decreasing,
# hence returns “True“.
A = [1, 2, 2, 3, 4, 7, 9]


# Python Program to check if given array is Monotonic

def isMonotonic(A):
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

print(isMonotonic(A))


#Approach 3 – By checking length of the array

def isMonotonic(arr):
    if len(arr) <= 2:
        return True
    direction = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if direction == 0:
            direction = arr[i] - arr[i - 1]
            continue
        if (direction > 0 and arr[i] < arr[i - 1]) or (direction < 0 and arr[i] > arr[i - 1]):
            return False
    return True

# Example usage

arr3 = [1, 2, 2, 2, 3, 4] # True

print(isMonotonic(arr3)) # should return True
