
class Circle:

    pi=3.14

    def __init__(self,Radius=0.0,Area=0.0,Circumference=0.0):
        self.radius=Radius
        self.area=Area
        self.Circumference=Circumference

    def Accept(self,Radius):
        self.radius=Radius       

    def CalculateArea(self):
        self.area=Circle.pi*self.radius*self.radius
        
    def CalculateCircumference(self):
        self.Circumference=2*Circle.pi*self.radius
        
    def Display(self):
        print("Value of radius: ",self.radius)
        print("Area of circle: ",self.area)
        print("Circumference of circle: ",self.Circumference)

def main():

    obj1=Circle()
    obj1.Accept(25)
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

    obj2=Circle()
    obj2.Accept(5)
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()

if __name__=="__main__":
    main()
