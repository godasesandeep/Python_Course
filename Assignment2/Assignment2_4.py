
def main():
    n=int(input("Enter number for addition of factor: "))
    factor=[]
    for i in range(1,n):
        if(n%i==0):
            factor.append(i)

    sum=0
    for value in factor: 
        sum=sum+value
    print(sum)           
            


if __name__=="__main__":
    main()            
