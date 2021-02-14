from User import User
from Account import Account
from Employee import Employee
from Service import Service
from utilities import Utilities
from constants import USER_FILE_PATH, ROOT_DIR, SERVICE_FILE_PATH
import sys



class mainBankingApp:
    def __init__(self):
        self.user = User()
        self.account = Account()
        self.employee = Employee()
        self.service = Service()
        self.utilities = Utilities()
        self.initAmt = 0


    def runProg(self):
        self.user.creatingNewUser()
        while True:

            # os.system("cls")
            print("************************************************************")
            print("Choose 'a' to create new account and deposit some initial amount")
            print("Choose 'b' to deposit amount:")
            print("Choose 'c' to withdraw amount")
            print("Choose 'd' to apply for a loan")
            print("Choose 'e' to know your application decision")
            print("************************************************************")


            optionChosen = input("\nPlease enter one of the options above\n")
            # print(optionChosen)
            if optionChosen == 'a':
                self.initAmt = eval(input("Please insert a amount to start an Account:\n "))
                # print(self.initAmt)
                self.account.initial_deposit(self.initAmt)

            elif optionChosen == 'b':
                print("Your current account balance is :", self.initAmt)
                depositAmt = input("\nPlease enter the amount to deposit:")
                self.account.deposit(depositAmt)
            elif optionChosen == 'c':
                wamount = input("Enter amount to withdraw: ")
                self.account.withdraw(wamount)
            elif optionChosen == 'd':
                inputData = self.service.newLoanApplication()
                self.service.savingToJsonFile(inputData)
            elif optionChosen == 'e':
                self.employee.verifyApplicationForApproval()
                break




if __name__ == '__main__':
    mainApp = mainBankingApp()
    mainApp.runProg()