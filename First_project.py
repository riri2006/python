class Bankaccount:
    def __init__(self,balance, pin):
        self.__balance = balance
        self.pin = pin

    def Deposit(self,amnt):
        self.deposit=amnt
        print(f"Deposited {amnt} successfully")
        self.__balance = self.__balance + self.deposit

    def Withdraw(self,withdraw_amount):
        self.withdraw = withdraw_amount
        if(self.__balance>= withdraw_amount):
            print("Withdrawn", self.withdraw,"Successfully..")
            self.__balance -= withdraw_amount
        else:
            print("INSUFFICIENT BALANCE")

    def getbalance(self):
        return self.__balance


pin = int(input("Enter your PIN number: "))
balance = int(input("Enter the current balance: "))


if (pin != 1234):
        print("INVALID CREDENTIALS")


else:
        w1 = Bankaccount(balance,pin)

        while True:

            print("Choose")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Check current balance")

            user = int(input("Enter the option:"))

            if(user==1):
                wd_amount = int(input("Enter withdraw amount: "))
                w1.Withdraw(wd_amount)
                print("Current balance:" , w1.getbalance())

            elif(user == 2):
                d_amount = int(input("Enter deposit amount: "))
                w1.Deposit(d_amount)
                print("Current balance:" , w1.getbalance())

            elif(user==3):
                print("Current Balance: ", w1.getbalance())

            else:
                print("INVALID OPTIONS..")

        

