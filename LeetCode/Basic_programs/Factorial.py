#Factorial Using recursive method

num=5

def factorial(num):
    if num<0:
        return 0
    return 1 if (num==1 or num==0) else num*factorial(num-1)

print("Factorial of",num,"is",factorial(num))



#Factorial of a Number Using Iterative approach

def factorial_while(n):
    if n<0:
        return 0
    elif n==1 or n==0:
        return 1
    else:
        fact =1
        while(n>1):
            fact *=n # fact =fact*n
            n -=1    #n=n-1
        return fact
    
print("Factorial of",num,"is",
factorial_while(num))


# Function to find factorial of given number using for loop
def factorial_for(n):
       
    fact = 1
      
    for i in range(2, n+1):
        fact *= i  #fact= fact*i
    return fact

print("Factorial of", num, "is",
factorial_for(num))