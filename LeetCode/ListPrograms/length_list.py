
lst = [1, 2, 3, 4, 5]

# Define a function to count the number of elements in a list using recursion

def count_elements_recursion(lst):
    if not lst:
        return 0
    return 1 + count_elements_recursion(lst[1:])

print(count_elements_recursion(lst))


# Using for loop

def length_list(lst):
    counter=0
    for i in lst:
        counter +=1
    return counter

print(length_list(lst))

# Using for loop
print(sum(1 for _ in lst))

print([1 for _ in lst])