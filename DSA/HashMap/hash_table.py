

class HashTable:

    def __init__(self):
        self.MAX=10
        self.arr=[None for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.MAX
    
    def __setitem__(self,key,value):
        index=self.get_hash(key)
        self.arr[index]=value

    def __getitem__(self,key):
        index=self.get_hash(key)
        return self.arr[index]
    
    def __delitem__(self,key):
        index=self.get_hash(key)
        self.arr[index]=None

        
    


dic=HashTable()

dic["1"]="Sandeep"
#dic.add("2","Harshad")
#dic.add("3","Shridhar")
dic["captain"]="pravin"
dic["march 6"]=39
#dic['march 17']=40
dic["2"]="Harshad"
dic["3"]="Shridhar"
print(dic["1"])
print(dic["captain"])
del dic["3"]
print(dic.arr)



