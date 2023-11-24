
def main():
    n=int(input("Enter number: ")) 
    for i in range(2,n):                
        if(n % i==0):          
         print("Number is not prime:")
         break
    else:         
        print("Number is prime:") 
if __name__=="__main__":
    main()               