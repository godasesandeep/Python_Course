#Python Program to Find Sum of Array Using reduce method
from functools import reduce
arr = [12, 12, 3, 4, 15, 15]

sum = reduce(lambda a,b :a+b,arr)

print(sum)

#Python Program to Find Sum of Array Using enumerate function
arr = [12, 12, 3, 4, 15, 15]
sum=0
for i,a in enumerate(arr): # enumerate gives index "i" and list value "a"
    sum=sum+a
print(sum)

##Python Program to Find Sum of Array Using Counter() class

from collections import Counter
arr = [12, 12, 3, 4, 15, 15]

c= Counter(arr)
sum=0
for value,i in c.items(): #c.items() gives value i.e element in list and i gives the number of occurance of element
    sum=sum +value*i
print(sum)


#Python Program to Find Sum of Array Using Divide and conquer

def sum_of_array(arr, low, high):
    if low == high:
        return arr[low]
    mid = (low + high) // 2
    left_sum = sum_of_array(arr, low, mid)
    right_sum = sum_of_array(arr, mid+1, high)
    return left_sum + right_sum
#Examples
arr = [12, 12, 3, 4, 15, 15]
print(sum_of_array(arr, 0, len(arr)-1)) # Output: 6