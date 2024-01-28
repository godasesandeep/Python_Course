
class Cylinder:

    pi=3.14

    def __init__(self,r,l):
        self.r=r
        self.l=l

    def FaceArea(self):
        print("FaceArea area is:",2*Cylinder.pi*self.r*self.r)
        return 2*Cylinder.pi*self.r*self.r

    def SurfaceArea(self):
        print("SurfaceArea is: ",2*Cylinder.pi*self.r*self.l )
        return 2*Cylinder.pi*self.r*self.l

    def TotalArea(self):
        print("Total area is: ",self.FaceArea()+self.SurfaceArea())


def main():

    obj1=Cylinder(8,2)
    obj1.FaceArea()
    obj1.SurfaceArea()
    obj1.TotalArea()

    obj2=Cylinder(2,8)
    obj2.FaceArea()
    obj2.SurfaceArea()
    obj2.TotalArea()


if __name__=="__main__":
    main() 