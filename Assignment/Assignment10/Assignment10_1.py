
from sys import *
import os

def DirectoryFileSearch(DirName,FileExt):
    print("We are going to search the file in that location: ",DirName)
    flag=os.path.isabs(DirName)
    if flag==False:
        DirName=os.path.abspath(DirName)
    exist=os.path.exists(DirName)

    if exist:
        for foldername,subfoldername,filename in os.walk(DirName):
            #print("Current directory name",foldername)
            for fname in filename:
                if FileExt in fname:
                    print(fname)
    else:
        print("invalid path")

def main():
    print("------ Automation Script -----")
    print("Automation Script name: ",argv[0])
    
    if (len (argv)==2):
        if (argv[1]=="-h"):
            print("This Automation script is used to perform search of file with perticular extention")
            exit()
        elif (argv[1]=="-u"):
            print("usage name of script first name")
            print("example:DirectoryFileSearch.py 'Directory_Name' 'Extention'")
            exit()
        else:
            print("Invalid arguments")

    if (len (argv)!=3):
        print("Invalid number of arguments")
        exit()

    else:
        DirectoryFileSearch(argv[1],argv[2])
    
if __name__=="__main__":
    main()


        