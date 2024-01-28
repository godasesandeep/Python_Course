# This code finds the remainder of the product of all the elements in the array arr divided by 'n'.
def findremainder(arr, len, n):
    product = 1
    for i in range(len):
        product = product * arr[i]
    return product % n
 
 
arr = [100, 10, 5, 25, 35, 14]
len = len(arr)
n = 11
print(findremainder(arr, len, n))


#Approach that avoids overflow :

def findremainder1(arr, lens, n):

    mul = 1
    for i in range(lens): 
        mul = (mul * (arr[i] % n)) % n
    return mul % n

print( findremainder1(arr, len, n))
