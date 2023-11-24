def ChkNum(value):
    result=value%2
    if(result==0):
        print("Even number")
    else:
        print("Odd number")
def main():
    i=0
    print("Enter number : ")
    i=int(input())
    ChkNum(i)
if __name__=="__main__":
    main()

