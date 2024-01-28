import os

File_Name=input("Enter the file Name :")
flag1=os.path.exists(File_Name)
if flag1:
    Fobj=open(File_Name,'r')
    main_string = Fobj.read()
    print("Enter the String to search in ",File_Name)
    sub_string = input()
    count_er=0
    start_index=0
    for i in range(len(main_string)):
        j = main_string.find(sub_string,start_index)
        if(j!=-1):
            start_index = j+1
            i=j+1
            count_er+=1
        else:
            break

    print("Total occurrences are: ", count_er)

else:
    print("File doesnot Exist")