import os
from sys import *
import hashlib

def Compare(File1,File2):
    print("Start comparing")
    lst=[File1,File2]
    Flag1=os.path.exists(File1)
    Flag2=os.path.exists(File2)
    if (Flag1 and Flag2):
        out=[]
        for i in lst:
            out.append(CheckSum(i))

        if out[0]==out[1]:
            print("Sucess")
        else:
            print("Failer")
    else:
        print("File {} or {} not exist or both".format(File1,File2))

def CheckSum(i):
    Fobj1=open(i, 'rb')
    
    hasher = hashlib.md5()

    BUF_SIZE=1024

    buf1=Fobj1.read(BUF_SIZE)

    while len(buf1)>0:
        hasher.update(buf1)
        buf1=Fobj1.read(BUF_SIZE)
    Fobj1.close()
    Hash1=hasher.hexdigest()
    return Hash1


def main():
    print("-------------- Automation Script --------------")

    print("Automation Script Name : ",argv[0])

    if(len(argv) == 2):
        if(argv[1] == "-h" or argv[1] == "-H"):    # Flag for displaying help
            print("This automation script is used to Compare content of two files if same return Sucessful otherwise Failer")
            exit()
        
        elif(argv[1] == "-u" or argv[1] == "-U"):    # Flag for displaying the usage of script
            print("Usage : Name_Of_Script First_Argument Second_Argument")
            print("Example : Assignment9_4.py ABC.txt Demo.txt")
            exit()

        else:
            print("There is no such option to handle")
            exit()

    if(len(argv) != 3):
        print("Invalid number of arguments")
        exit()
    else:
        Compare(argv[1], argv[2])


if __name__=="__main__":
    main()