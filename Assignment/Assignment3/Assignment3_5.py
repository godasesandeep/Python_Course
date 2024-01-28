import MarvellousNum
from functools import reduce

def ListPrime():
    n=int(input("Enter Number of elements in List: "))
    List1=[]
    for i in range (n):
         m=int(input("Enter the number to add: "))
         List1.append(m)
    return List1

l2=ListPrime()

PrimeNum=list(filter( MarvellousNum.ChkPrime,l2))
print(PrimeNum)  
Add=lambda a,b:a+b 
Ans=reduce(Add,PrimeNum)

print(Ans)