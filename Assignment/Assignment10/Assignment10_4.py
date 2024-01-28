from sys import *
import os
import shutil

def DirectoryCopyExt(DirName1,DirName2,FileExt):
    print("We are going to Copy the file fron Dir1 to Dir2: ")
    flag=os.path.isabs(DirName1)
    if flag==False:
        DirName1=os.path.abspath(DirName1)
    exist=os.path.exists(DirName1)
    flag2=os.path.isabs(DirName2)
    if flag2==False:
        DirName2=os.path.abspath(DirName2)
    exist2=os.path.exists(DirName2)
    if exist2==False:
        os.mkdir(DirName2)

    if exist:
        for foldername,subfoldername,filename in os.walk(DirName1):
            #print("Current directory name",foldername)
            for fname in filename:
                if FileExt in fname:
                    # Source path
                    source = os.path.join(foldername,fname)
                    
                    # Destination path
                    destination =os.path.join(DirName2,fname)
                    
                    # Copy the content of
                    # source to destination
                    
                    try:
                        shutil.copyfile(source, destination)
                        print("{} copied successfully.".format(fname))
                    
                    # If source and destination are same
                    except shutil.SameFileError:
                        print("Source and destination represents the same file.")
                    
                    # If destination is a directory.
                    except IsADirectoryError:
                        print("Destination is a directory.")
                    
                    # If there is any permission issue
                    except PermissionError:
                        print("Permission denied.")
            
                    # For other errors
                    except:
                        print("Error occurred while copying file.")
    else:
        print("invalid path")



def main():
    print("------ Automation Script -----")
    print("Automation Script name: ",argv[0])
    
    if (len (argv)==2):
        if (argv[1]=="-h"):
            print("This Automation script is used to Copy file from one dirctory to another")
            exit()
        elif (argv[1]=="-u"):
            print("usage name of script first name")
            print("example:DirectoryFileSearch.py 'Directory_Name' 'Extention'")
            exit()
        else:
            print("Invalid arguments")

    if (len (argv)!=4):
        print("Invalid number of arguments")
        exit()

    else:
        DirectoryCopyExt(argv[1],argv[2],argv[3])
    
if __name__=="__main__":
    main()
