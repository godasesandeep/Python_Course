
from functools import reduce

def CheckEven(No):
    if(No % 2 == 0):
        return True
    else:
        return False
       

def Square(No):
    return No*No

def Add(A,B):
    return A+B

def main():
    Data = []

    P= int(input("Enter number of elements : "))
  
    print("Enter the elements : ")
    for i in range(P):
        Value = int(input())
        Data.append(Value)
    print("Input List: ",Data)
    
    a = list(filter(CheckEven,Data))
    print("List after filter: ",a)

    s = list(map(Square,a))
    print("List after map: ",s)

    result = reduce(Add,s)
    print("Output of reduce: ",result)

if __name__ == "__main__":
    main()