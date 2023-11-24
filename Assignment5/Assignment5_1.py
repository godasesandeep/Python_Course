
class Demo:

    value=1
    
    def __init__(self,No1,No2):
        self.no1=No1
        self.no2=No2

    def Fun(self):
        print("Display  First values: ",self.no1)
       
    def Gun(self):
        print("Display Second values: ",self.no2)

def main():

    obj1=Demo (3,2)
    obj2=Demo (4,6)

    obj1.Fun()
    obj2.Fun()

    obj1.Gun()
    obj2.Gun()

if __name__=="__main__":
    main()    
            