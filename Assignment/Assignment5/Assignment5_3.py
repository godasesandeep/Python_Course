
class Arithmetic:

    def __init__(self,value1=0,value2=0):
        self.value1=value1
        self.value2=value2

    def Accept(self,value1,value2):
        self.value1=value1
        self.value2=value2
        
    def Addition(self):
        print("Addition of two values: ",self.value1+self.value2)

    def Substration(self):
        print("Substraction of two values: ",self.value1-self.value2)

    def Multiplication(self):
        print("Multiplication of two values: ",self.value1*self.value2)

    def Division(self):
        print("Division of two values: ",self.value1/self.value2)


def main():
    obj1=Arithmetic(100,50)
    obj1.Addition()
    obj1.Substration()
    obj1.Multiplication()
    obj1.Division()

    obj2=Arithmetic()
    obj2.Accept(15,10)
    obj2.Addition()
    obj2.Substration()
    obj2.Multiplication()
    obj2.Division()

if __name__=="__main__":
    main()