
def main():
    n=int(input("Enter the numbers :"))
    List1=[]
    for i in range(n):
        p=int(input("Enter the number to add :"))
        List1.append(p)
    sum=0
    for i in List1:
        sum=sum+i
    print(sum)
if __name__=="__main__":
    main()    



