
import os 

def DisplayContent():
    File_Name =input("Enter the file name to display: ")
    flag1 = os.path.exists(File_Name)
    if flag1 :
        FContent = open(File_Name, "r")
        A = FContent.read()
        print(A)
        FContent.close()

def main():
    DisplayContent()



if __name__ == "__main__":
    main()