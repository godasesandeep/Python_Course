
class BankAccount:

    ROI=10.5

    def __init__(self,Name,Amount):
        self.name=Name
        self.amount=Amount

    def Display(self):
        print("Name is: ",self.name)
        print("Amount is: ",self.amount)
        

    def Deposit(self,value1):
        self.amount= self.amount+value1
        print("your account balance after deposite is: ",self.amount)

    def Withdraw(self,Amount):
        self.amount=self.amount-Amount

    def CalculateInterest(self):
        print("Calculate Interest per year: ",BankAccount.ROI*self.amount/100)

def main():
    obj1=BankAccount("Ashwini",5000)
    obj1.Display()
    obj1.Deposit(500)
    obj1.Withdraw(200)
    obj1.CalculateInterest()

    obj2=BankAccount("Radha",10000)
    obj2.Display()
    obj2.Deposit(5000)
    obj2.Withdraw(500)
    obj2.CalculateInterest()

if __name__=="__main__":
    main()
        