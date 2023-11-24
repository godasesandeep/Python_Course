
i=1
def Display(n):
    global i
    if i <=n:
        print("*",end=" ")
        i+=1
        Display(n)


def main():
    Display(5)


if __name__ =="__main__":
    main()
