from DatabasesConn import MySQLConnector


class User:
    def __init__(self):
        usertype = input("Enter if 'New User' or 'Customer' : ")
        self.dbConnect = MySQLConnector()

        if usertype == 'New User':
            n = input("Enter First Name, Last Name, Email, DOB('YYYY-MM-DD'), Phone#, SSN#, Username, Password: ")
            self.lst = [int(x) if x.isdigit() else x.strip() for x in n.split(',')]
            print(self.lst)
            self.newUser()

        elif usertype == 'Customer':
            self.username = input("Enter Username: ")
            self.password = input("Enter Password: ")
            self.customerFunc()


    def newUser(self):
        self.dbConnect.connect_to_db()
        column_names = self.dbConnect.getMySQLColumnNames('USER')
        print("Printing column names",column_names)
        print("Input list", self.lst)
        query = self.dbConnect.insertRows('USER', column_names, self.lst)
        print("Printing query from newUser: ",query)
        # self.dbConnect.executeQuery(query)



    def customerFunc(self):
        pass


if __name__ == '__main__':
    user = User()
    user.newUser()
