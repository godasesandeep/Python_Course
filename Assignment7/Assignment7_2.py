
import threading

def Evenfactor(n1):
    sum=0
    for i in range(1,n1+1):
        if n1%i==0:
            if i%2==0:
                sum=sum+i
    print("Addition of Even factor is : ",sum)


def Oddfactor(n2):
    sum=0
    for i in range(1,n2+1):
        if n2%i==0:
            if i%2!=0:
                sum=sum+i
    print("Addition of Odd factor is : ",sum)


def main():

    number=12 #1,2,3,4,6,12 even=24 odd=4
    t1=threading.Thread(target=Evenfactor,args=(number,))
    t2=threading.Thread(target=Oddfactor,args=(number,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    print("Exit from main")




if __name__=="__main__":
    main()