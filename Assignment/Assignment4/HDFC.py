
class HDFC:

    ROI=9

    def __init__ (self,Name,Amount):
        self.name=Name
        self.amount=Amount
        print("Constructor calling....")

    def DisplayBalance(self):
        print("your current Balance is: ",self.amount)

    def Deposite(self,Value1):
        self.amount= self.amount+Value1
        print("your account balance after deposite is: ",self.amount)

    def Withdraw(self,value2):
        if(self.amount < value2):
            print("No Sufficent balance in your account")
        else:
            self.amount = self.amount-value2
            print("Your account is debited:",value2)
             

def main():

    obj1=HDFC("Ashwini",1000) #obj1.name="Ashwini",obj1.amount=1000
    obj1.Withdraw(500)
    obj1.DisplayBalance()
    obj1.Deposite(4000)
    obj1.DisplayBalance()





    #obj2=HDFC("Sandeep",5000) ##obj2.name="Sandeep",obj1.amount=5000


if __name__=="__main__":
    main()



          