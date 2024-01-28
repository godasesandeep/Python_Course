import threading

def Evenlist(list1):
    sum=0
    for i in list1:
        if i%2==0:
            sum=sum+i
    print("Addition of Even number in list is : ",sum)


def Oddlist(list1):
    sum=0
    for i in list1:
        if i%2!=0:
            sum=sum+i
    print("Addition of Odd number in list is : ",sum)


def main():

    numberlist=[1,2,3,4,6,12,9] # even=24 odd=13
    t1=threading.Thread(target=Evenlist,args=(numberlist,))
    t2=threading.Thread(target=Oddlist,args=(numberlist,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__=="__main__":
    main()