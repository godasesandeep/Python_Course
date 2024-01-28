
from functools import reduce

def GreaterEqual(No):
    if (No >= 70) and (No <= 90):
        return True 
    else:
        return False
    
def Increase(No):
    return No+10
                          
def Product(A,B):
    return A*B

def main():
    Data = []

    P= int(input("Enter number of elements : "))
  
    print("Enter the elements : ")
    for i in range(P):
        Value = int(input())
        Data.append(Value)
    print("Input List: ",Data)
    
    a = list(filter(GreaterEqual,Data))
    print("List after filter: ",a)

    s = list(map(Increase,a))
    print("List after map: ",s)

    result = reduce(Product,s)
    print("Output of reduce: ",result)

if __name__ == "__main__":
    main()