
import os

def CheckFileExist():
    File_name = input("Enter the name of file that you want Check : ")

    if os.path.exists(File_name):

        print("File is exist")

    else:
    
        print("File is not exist in current directory")

def main():
    
    CheckFileExist()
    
if __name__ == "__main__":
    main()