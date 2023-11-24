

from functools import reduce

def PrimeNum(N):
    if N==1:
        return False
    for i in range(2,N):
        if(N % i ==0):
            return False
    else:
        return True

def Multiply(No):
    return No*2

def Maximum1(a,b):
    if a > b :
        return a
    else:
        return b   

def main():
    Data = []

    P= int(input("Enter number of elements : "))
  
    print("Enter the elements : ")
    for i in range(P):
        Value = int(input())
        Data.append(Value)
    print("Input List: ",Data)

    
    a = list(filter(PrimeNum,Data))
    print("List after filter: ",a)

    s = list(map(Multiply,a))
    print("List after map: ",s)

    output=reduce(Maximum1,s)
    print("output of reduce: ",output)

    

if __name__ == "__main__":
    main()