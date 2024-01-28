
def main():
    n=int(input("Enter number :"))  
    for i in range(n):           
        for j in range(n-i):
            print("* ",end="")
        print( )
if __name__=="__main__":
    main()          
