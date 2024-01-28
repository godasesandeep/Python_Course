
class Calculator:

    def __init__ (self,A,B): 
        self.a=A
        self.b=B

    def Add(self):
        print("Addition of two numbers: ",self.a+self.b)

    def Sub(self):
        print("Substration of two numbers:",self.a-self.b)

    def Mul(self):
        print("Multiplication of two numbers: ",self.a*self.b)

    def Div(self):
        print("Division of two numbers: ",self.a/self.b)

def main():

    a=Calculator(50,25)

    a.Add()
    a.Sub()
    a.Mul()
    a.Div()
    
    b=Calculator(5,3)

    b.Add()
    b.Sub()
    b.Mul()
    b.Div()
    

if __name__=="__main__":
    main()             
           