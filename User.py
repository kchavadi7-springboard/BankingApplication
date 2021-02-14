# from DatabasesConn import MySQLConnector
from constants import USER_FILE_PATH
import random
from utilities import Utilities

class User:
    def __init__(self):
        self.utilities = Utilities()

    def creatingNewUser(self):
        n = input("Enter First Name, Last Name, Email, DOB('YYYY-MM-DD'), Phone#, SSN#, Username, Password:\n ")
        lst = [int(x) if x.isdigit() else x.strip() for x in n.split(',')]
        customerId = random.randint(1, 10000)
        lst.insert(0, customerId)
        print(lst)
        self.utilities.savingToJsonFile(lst, USER_FILE_PATH)
        print("Your customer ID is: ", customerId)



    # def newUser(self):
    #     self.dbConnect.connect_to_db()
    #     column_names = self.dbConnect.getMySQLColumnNames('USER')
    #     print("Printing column names",column_names)
    #     print("Input list", self.lst)
    #     query = self.dbConnect.insertRows('USER', column_names, self.lst)
    #     print("Printing query from newUser: ",query)
    #     # self.dbConnect.executeQuery(query)



if __name__ == '__main__':
    user = User()
    user.creatingNewUser()
