
class BookStore:

    NoOfBooks=0

    def __init__(self,Name=input("Enter Name: "),Author=input("Enter Name of Authour :")):
        self.name=Name
        self.author=Author
        self.noOfBooks=BookStore.NoOfBooks+1
    NoOfBooks=+1

    def Display(self):
        print( "{0} by {1}".format(self.name,self.author), end='')
        print(". Number of Books is: ",self.NoOfBooks)

def main():
    obj1=BookStore("Linux system programming","Robert Love")
    obj1.Display()

    obj2=BookStore("C Programming","Dennis Ritchie")
    obj2.Display()

if __name__=="__main__":
    main()