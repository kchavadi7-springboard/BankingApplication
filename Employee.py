import os
import json

class Employee:
    global ROOT_DIR
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    def checkAnyNewApplication(self):
        fetchFilePath = os.path.join(ROOT_DIR, 'JsonDataFIles/serviceData.json')
        # print(fetchFilePath)
        fileSize = os.path.getsize(fetchFilePath)
        # print(fileSize)

        if os.stat(fetchFilePath).st_size == 0:
            print("File is empty")
        else:
            f = open(fetchFilePath)
            applicationJson = json.load(f)
            # print(applicationJson)
        return applicationJson


    def verifyApplicationForApproval(self):
        application = self.checkAnyNewApplication()
        print("\n -------Application Decision-------\n")
        for v in application.values():
            salary, dependants, company = int(v[1]), int(v[2]), v[3]
            if dependants == 0 and salary >= 20000:
                print("Loan Approved")
            elif (0 < dependants <= 2) and salary >= 45000 and len(company) > 0:
                print("Loan Approved")
            else:
                print("Loan Not Approved")








        # print({val[i]:val[i] for i in range(len(val))})












if __name__ == '__main__':
    employee = Employee()
    employee.verifyApplicationForApproval()
