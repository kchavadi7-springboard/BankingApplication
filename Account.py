

class Account:

    def __init__(self, balance=0):
        self.balance = balance
        print(self.balance)



    def initial_deposit(self, amount):
        self.balance = self.balance + amount
        print("Your new account balance now is: ", self.balance)


    def deposit(self, depoamt):
        self.balance += int(depoamt)
        print("-----Deposit Successful!-----")
        print("Your new account balance is: ", self.balance)


    def withdraw(self, withdrawamt):

        if int(withdrawamt) > self.balance:
            deposition = input("Please deposit more amount as your balance is insufficient: ")
            self.balance += int(deposition)
            print("Your current balance is: {}", self.balance)
        else:
            self.balance -= int(withdrawamt)
            print("-----Withdrawal successfully!-----")
            print("Your current account balance is: ", self.balance)





if __name__ == '__main__':
    account = Account()
    initAmt = eval(input("Please insert a amount to start an Account: "))
    print(initAmt)
    account.initial_deposit(initAmt)

    print("Your current account  balance is :", initAmt)
    depositAmt = input("Please enter the amount to deposit:")
    account.deposit(depositAmt)

    wamount = input("Enter amount to withdraw: ")
    account.withdraw(wamount)
