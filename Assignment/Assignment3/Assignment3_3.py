
def minimum():
    n=int(input("Enter the numbers :"))
    List3=[]
    for i in range(n):
        a=int(input("Enter the number to add :"))
        List3.append(a)
    s=List3[0]
    l=len(List3) 
    for i in range(1,l):
        if s < List3[i]:
            continue
        else:
            s= List3[i]
    print(s)
       
minimum()          

