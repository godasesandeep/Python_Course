#Add two number using lambda function
num1=5
num2=2
add_num = lambda num1,num2:num1+num2

result=add_num(num1,num2)

print("addition of two number {} and {} using lambda function is {}".format(num1,num2,result)) 

#Add two number using recursive method

def add_recursive(num1,num2):
    if num1==0:
        return num2
    else:
        return add_recursive(num1-1,num2+1)
    
result=add_recursive(num1,num2)

print(f"addition of two number {num1} and {num2} using recursive method is {result} ")

# Adding two nos using operator 

import operator
result = operator.add(num1,num2)
 
print(f"addition of two number {num1} and {num2} using operator module is {result} ")