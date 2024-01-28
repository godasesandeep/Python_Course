class HashTableCollision:

    def __init__(self):
        self.MAX=10
        self.arr=[[] for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.MAX
    
    def __setitem__(self,key,value):
        index=self.get_hash(key)
        found=True
        for idx,element in enumerate(self.arr[index]):
            if len(element)==2 and element[0]==key:
                self.arr[index][idx]=(key,value)
                found=False
        if found:
            self.arr[index].append((key,value))

    def __getitem__(self,key):
        index=self.get_hash(key)
        for idx,element in enumerate(self.arr[index]):
            if len(element)==2 and element[0]==key:
                return self.arr[index][idx][1]  #this is also working
                #return element[1]
        else:
            print("Iteam not found")
    
    def __delitem__(self,key):
        index=self.get_hash(key)
        for idx,element in enumerate(self.arr[index]):
            if element[0]==key:
                self.arr[index].pop(idx)
        

        

dic=HashTableCollision()

dic["1"]="Sandeep"
#dic.add("2","Harshad")
#dic.add("3","Shridhar")
dic["captain"]="pravin"
dic["march 6"]=39
dic['march 17']=40
del dic['march 17']
dic["2"]="Harshad"
#del dic["2"]
dic["3"]="Shridhar"
print(dic["1"])
print(dic["captain"])
#del dic["3"]
print(dic.arr)