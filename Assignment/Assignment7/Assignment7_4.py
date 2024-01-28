
import threading
import os


def Digitcount(str1):
    count=0
    for i in str1:
        if i.isdigit():
            count=count+1
    print("Number of digit is",count)
    print("Digitcount assigned to thread: {}".format(threading.current_thread().name))
    print("ID of Thread running Digitcount: {}".format(threading.get_ident()))


def Smallcount(str1):
    count=0
    for i in str1:
        if i.islower():
            count=count+1
    print("Number of Small letter is",count)
    print("Smallcount assigned to thread: {}".format(threading.current_thread().name))
    print("ID of Thread running Smallcount: {}".format(threading.get_ident()))


def Capitalcount(str1):
    count=0
    for i in str1:
        if i.isupper():
            count=count+1
    print("Number of Capital letter is",count)
    print("Capitalcount assigned to thread: {}".format(threading.current_thread().name))
    print("ID of Thread running Capitalcount: {}".format(threading.get_ident()))


def main():
    string1="HapPy BirThady Sir 1234"
    t1=threading.Thread(target=Digitcount,args=(string1,))
    t2=threading.Thread(target=Smallcount,args=(string1,))
    t3=threading.Thread(target=Capitalcount,args=(string1,))

    t1.start()
    t2.start()
    t3.start()
    
    t2.join()
    t1.join()
    t3.join()



if __name__=="__main__":
    main()