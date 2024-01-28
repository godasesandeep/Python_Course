arr=[7,2,5,9,4,3,8,6,1]

def merge_sort(arr,l,r):
    if(l<r):
        mid=(l+r)//2
        merge_sort(arr,l,mid)
        merge_sort(arr,mid+1,r)
        merge(arr,l,mid,r)


def merge(arr,l,mid,r):
    n1=mid-l+1
    n2=r-mid
    rarr=[]
    larr=[]
    for i in range(n1):
        rarr.insert(i,arr[l+i])
    for j in range(n2):
        larr.insert(j,arr[mid+1+j])

    x=0
    y=0
    z=l
    while(n1>x and n2>y):
        if rarr[x]<larr[y]:
            arr[z]=rarr[x]
            x +=1
            z +=1
        else:
            arr[z]=larr[y]
            y+=1
            z+=1

    while(n1>x):
        arr[z]=rarr[x]
        x+=1
        z+=1

    while(n2>y):
        arr[z]=larr[y]
        y+=1
        z+=1

merge_sort(arr,0,len(arr)-1)
print(arr)