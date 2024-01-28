import threading

def Even(n1):
    count=0
    for i in range(1,n1):
        if i%2==0:
            count=count+1
            print("{} Even number is : {}".format(count,i))
    
def Odd(n2):
    count=0
    for i in range(1,n2):  
        if i%2!=0:
            count=count+1
            print("{} Odd number is : {}".format(count,i))


def main():

    number=21

    t1=threading.Thread(target=Even,args=(number,))
    t2=threading.Thread(target=Odd,args=(number,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__=="__main__":
    main()