
i=0
sum =0
def Display(n):
    global i
    global sum
    if i <len(n):
        sum =sum +int(n[i])
        if i==(len(n)-1):
            print(sum)
        i+=1
        Display(n)



def main():
    n=input("Enter the number to sum: ")
    Display(n)


if __name__ =="__main__":
    main()
