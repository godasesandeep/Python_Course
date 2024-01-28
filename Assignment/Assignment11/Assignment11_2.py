import os
from sys import *
import hashlib
import time

def DisplayDupLog(DirName):
    print("Display CheckSums of file")
    flag=os.path.isabs(DirName)
    if flag==False:
        DirName=os.path.abspath(DirName)
    exist=os.path.exists(DirName)
    dup={}
    if exist:
        for foldername,subfoldername,filename in os.walk(DirName):
            #print("Current directory name",foldername)
            for fname in filename:
                fpath=os.path.join(foldername,fname)
                hash=CheckSum(fpath)
                if hash in dup:
                    dup[hash].append(fpath)
                else:
                    dup[hash]=[fpath]
        Dupfiles=list(filter(lambda x:len(x)>1,dup.values()))
        seperator="*"*80
        obj1=open('Log.txt','a')
        obj1.write('\n'+seperator+'\n')
        obj1.write("Log start at : %s"%(time.ctime()))
        obj1.write('\n'+seperator+'\n')

        for dup in Dupfiles:
            for i in dup:
                obj1.write(i+'\n')

        obj1.close()
            
            

    else:
        print("invalid path")

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
            print("This automation script is used to Display Checksum of all the Files")
            exit()
        
        elif(argv[1] == "-u" or argv[1] == "-U"):    # Flag for displaying the usage of script
            print("Usage : Name_Of_Script First_Argument ")
            print("Example : Assignment9_4.py FolderPath ")
            exit()

        else:
            DisplayDupLog(argv[1])

    if(len(argv) != 2):
        print("Invalid number of arguments")
        exit()
        


if __name__=="__main__":
    main()