
from sys import *
import os

def DirectoryRename(DirName,FileExt1,FileExt2):
    print("We are going to Change  the file extention {} to {} in that location: {} ".format(FileExt1,FileExt2,DirName))
    flag=os.path.isabs(DirName)
    if flag==False:
        DirName=os.path.abspath(DirName)
    exist=os.path.exists(DirName)

    if exist:
        for foldername,subfoldername,filename in os.walk(DirName):
            #print("Current directory name",foldername)
            for fname in filename:
                if FileExt1 == fname[-len(FileExt1):]:
                    Source=os.path.join(foldername,fname)
                    dest=os.path.join(foldername,fname.replace(fname[-len(FileExt1):],FileExt2))
                    os.rename(Source,dest)

    else:
        print("invalid path")

def main():
    print("------ Automation Script -----")
    print("Automation Script name: ",argv[0])
    
    if (len (argv)==2):
        if (argv[1]=="-h"):
            print("This Automation script is used to Change  the file extention")
            exit()
        elif (argv[1]=="-u"):
            print("usage name of script first name & 'Extention1' is replaced with 'Extention2'")
            print("example:Assignment10_2.py 'Directory_Name' 'Extention1' 'Extention2'")
            exit()
        else:
            print("Invalid arguments")

    if (len (argv)!=4):
        print("Invalid number of arguments")
        exit()

    else:
        DirectoryRename(argv[1],argv[2],argv[3])
    
if __name__=="__main__":
    main()


        