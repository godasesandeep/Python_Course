#To find max number using ternary operator 

num1=5
num2=2

print(num1 if num1>=num2 else num2)


#maximum of two numbers using lambda function
 
maximum = maximum = lambda a,b:a if a > b else b
print(f'using lambda function: {maximum(num1,num2)} is a maximum number')
