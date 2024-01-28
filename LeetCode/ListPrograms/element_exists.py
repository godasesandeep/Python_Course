
#checking if element 7 is present

lst=[ 1, 6, 3, 5, 3, 4 ] 

i=7

if i in lst:
    print("Element Exist")
else:
    print("Element not exists")


#Find if an element exists in the list using the count() function
    
count_ele=lst.count(5)

if count_ele>0:
    print("Element Exist")
else:
    print("Element not exists")


