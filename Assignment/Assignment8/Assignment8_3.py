
i=1
def Display(n):
    global i
    if n >=i:
        print(n,end=" ")
        n-=1
        Display(n)



def main():
    Display(5)


if __name__ =="__main__":
    main()
