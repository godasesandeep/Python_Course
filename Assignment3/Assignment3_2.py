
def maximum():
    n=int(input("Enter the numbers :"))
    List2=[]
    for i in range(n):
        a=int(input("Enter the number to add :"))
        List2.append(a)
    b=List2[0]
    l=len(List2) 
    for i in range(1,l):
        if b > List2[i]:
            continue
        else:
            b= List2[i]
    print(b)
       
maximum()          

