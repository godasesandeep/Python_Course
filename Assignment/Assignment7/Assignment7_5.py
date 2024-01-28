import threading


def thread1(no1):
    for i in range(1,no1+1):
        print(i)

def thread2(no1):
    for i in range(no1,0,-1):
        print(i)


def main():

    t1=threading.Thread(target=thread1,args=(50,))
    t2=threading.Thread(target=thread2,args=(50,))
    t1.start()
    t1.join()
    print("Thread2 Started .....")
    t2.start()
    t2.join()

if __name__=="__main__":
    main()