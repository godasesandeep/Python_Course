
def main():
    n=int(input("Enter number for factorial: "))
    i=1
    j=1
    while(j<=n):
        i=i*j
        j=j+1
    print(i) 
    
if __name__=="__main__":
    main()
