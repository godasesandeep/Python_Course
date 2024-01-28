# type -1 --Python program to left-rotate the given array

def reverse(arr,start=0,end=None):
    if end==None:
        end =len(arr)-1
    else:
        end=end-1
    number_of_rotation=end-start+1
    count=0
    while(number_of_rotation//2 !=count):
        arr[start+count],arr[end-count] = arr[end-count],arr[start+count]
        count=count+1
    return arr

arr=[1,2,3,4,5,6,7,8]

#print(reverse(arr,0))  #start is include ,end is exclud, same as range function

def left_rotate_array(arr,sub_array_size):

    #reverse array
    arr=reverse(arr)

    # Reverse the First sub-array
    end=len(arr)-sub_array_size
    arr=reverse(arr,0,end)

    # Reverse the Second sub-array
    start=len(arr)-sub_array_size
    arr=reverse(arr,start)

    return arr

arr1=[1,2,3,4,5,6,7,8]
print("Orignal Arry",arr1)
print("Left rotate array by 3 :",left_rotate_array(arr1,3))



#type -2 --slicing approach to rotate the array

def sclice_left_rotate_array(arr,sub_array_size):
    arr1=arr[sub_array_size:] + arr[:sub_array_size]
    print(arr1)

sclice_left_rotate_array(arr,3)


#type -3 --function to rotate array by d elements using temp array

def rotate_array(arr,d):
    n=len(arr)
    temp=[]
    i=0
    while(d>i):
        temp.append(arr[i])
        i=i+1
    i=0
    while(n>d):
        arr[i]=arr[d]
        d=d+1
        i=i+1
    arr1=arr[:n-len(temp)]+temp
    return arr1

arr=[1,2,3,4,5,6,7,8]
print("Array after left rotation is: ", end=' ')
print(rotate_array(arr,3))

