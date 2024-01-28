arr=[7,8,1,3,5,2,4,6]

def merge_sort(arr,l,r):

    if (l<r):
        mid=(l+r)//2
        merge_sort(arr,l,mid) # selecting left half
        merge_sort(arr,mid+1,r) #Selecting Right half
        merge(arr,l,mid,r)      #Merge

def merge(arr,l,mid,r): #arr,0,0,1 #arr,2,2,3
    n1=mid-l+1
    n2=r-mid
    rarr=[]
    larr=[]
    for i in range(n1):
        larr.insert(i,arr[l+i])

    for j in range(n2):
        rarr.insert(j,arr[mid+1+j])

    x =0
    y =0
    z =l

    while(x<n1 and y<n2):
        if(larr[x]<=rarr[y]):
            arr[z]=larr[x]
            x += 1
        else:
            arr[z]=rarr[y]
            y += 1
        
        z += 1

    while(x<n1):
        arr[z]=larr[x]
        x += 1
        z += 1

    while(y<n2):
        arr[z]=rarr[y]
        y += 1
        z += 1



merge_sort(arr,0,len(arr)-1)
print(arr)