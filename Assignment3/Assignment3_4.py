
def main():
    n=int(input("Number of elements: "))
    Result=[]
    for i in range (n):
         m=int(input("Enter the number to add: "))
         Result.append(m)

    print(Result)
    print("Enter the element you want to search: ")
    p=int(input())
    count=0
    for i in Result:
        if(p==i):
            count=count+1
    print("Frequency of number in list: " ,count)


if __name__=="__main__":
    main()        