
def Factor():
    x=int(input("Enter the number: "))
    list1=[]
    for i in range(1,x+1):
        if(x % i ==0):
            list1.append(i)
    print(list1)
           

Factor()            


def Prime():
     x=int(input("Enter the number: "))
     for i in range(2,x):
         if(x % i==0):
             print("not prime")
             break
     else:
         print("prime number")
             
#Prime()             
    

