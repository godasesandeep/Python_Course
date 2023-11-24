
def Fact(n):
    if n==0:
        return 1
    return n*Fact(n-1)


def main():
    n=int(input("Enter the number : "))
   
    print(Fact(n))

    


if __name__ =="__main__":
    main()
