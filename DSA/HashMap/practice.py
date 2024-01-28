
arr=[[] for i in range(4)]
for i in range(4):
    if i!=1:
        arr[i].append((i,2))
#arr[1][1].append((3,4))

print(arr)
print(arr[1]) # get list @ index1
print(len(arr[1]))
for idx,ele in enumerate(arr[1]):
    print(idx,ele,len(ele))

'''
l1 = ["eat", "sleep", "repeat"]
l2=[[(1,2),(3,4),(10,22),(23,34)]]
print(l2[0][1])
l3=(1,2,3,4)
print(len(l3))

#print(list(enumerate(l1)))
#print(list(enumerate(l2)))
print(l2)
for i,j in enumerate(l2[0]):
    print(i,j)
    '''