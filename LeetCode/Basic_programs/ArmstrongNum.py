# It's a number that equals the sum of its digits, 
#each raised to a power. For example, if you have a number like 153, 
#it's an Armstrong number because 1^3 + 5^3 + 3^3 equals 153.


Num=153

x=Num
y=len(str(Num))  #Order of number 3 
sum=0
while(x!=0):
    r= x%10   # find the reminder of number ex: 153%10 gives reminder 3.
    sum=sum + r**y   #add the cube of a number to the sum1(3*3*3)
    x=x//10   #Then the step gives the quotient of the number (153//10=15).

if Num == sum:
    print("The given number", Num, "is armstrong number")
else:
    print("The given number", Num, "is not armstrong number")



def power(x,y): #x^y
    if y==0:
        return 1
    if y%2==0:
        return power(x,y//2)*power(x,y//2)
    else:
        return x*power(x,y//2)*power(x,y//2)



def order(num): #153
    index=0
    r=1
    while(num!=0):
        index +=1
        num=num//10
    return index

print(order(12344567))

def isArmstrong(num):
    o=order(num)
    r=num%10
    num=num//10
    sum=sum + power(r,o)




