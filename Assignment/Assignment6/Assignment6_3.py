
class Numbers:


    def __init__(self,value):
        self.value=value


    def ChkPrime(self):  
        n=self.value
        for i in range(2,n):
            if self.value % i==0:
                v= False
                break
        else:
            v= False
        return v
    

    def ChkPerfect(self):
        n=self.value
        sum=0
        for i in range(1,n):
            if self.value % i==0:
                sum=sum+i
        if sum==self.value:
            return True
        else:
            return False

    def Factors(self):
        n=self.value
        fact=[]
        for i in range(2,n):
            if self.value % i==0:
                fact.append(i)
        print("Factor of {0} number is : {1}".format(self.value,fact))


    def SumFactors(self):
        n=self.value
        sum=0
        for i in range(1,n):
            if self.value % i==0:
                sum=sum+i
        print("Sum of the factor is :", sum)
    

    

def main():
    obj1=Numbers(6)
    print(obj1.ChkPrime())
    print(obj1.ChkPerfect())
    obj1.Factors()
    obj1.SumFactors()

    obj2=Numbers(7)
    print(obj2.ChkPrime())
    print(obj2.ChkPerfect())
    obj2.Factors()
    obj2.SumFactors()

if __name__=="__main__":
    main()