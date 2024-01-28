#py Assignment9_3.py ABC.txt Demo.txt
import os
from sys import *

def CopyFile(Org_File,Copy_File):
    flag1=os.path.exists(Org_File)
    flag2=os.path.exists(Copy_File)
    if flag1:
        OContent=open(Org_File,"r")
        if flag2:
            CContent=open(Copy_File,"a")
        else:
            CContent=open(Copy_File,"x")
            print("File is sucessfuly Created : ", Copy_File)
        CContent.write(OContent.read())
        CContent.close()
        OContent.close()
        print("{} file content  is sucessfuly Copied to {}:".format(Org_File,Copy_File))

    else:
        print("File doesnot exist :",Org_File)



def main():
    print("-------------- Automation Script --------------")

    print("Automation Script Name : ",argv[0])

    if(len(argv) == 2):
        if(argv[1] == "-h" or argv[1] == "-H"):    # Flag for displaying help
            print("This automation script is used to Copy all content from existing file into new file")
            exit()
        
        elif(argv[1] == "-u" or argv[1] == "-U"):    # Flag for displaying the usage of script
            print("Usage : Name_Of_Script First_Argument Second_Argument")
            print("Example : Assignment9_3.py ABC.txt Demo.txt")
            exit()

        else:
            print("There is no such option to handle")
            exit()

    if(len(argv) != 3):
        print("Invalid number of arguments")
        exit()
    else:
        CopyFile(argv[1], argv[2])


if __name__=="__main__":
    main()