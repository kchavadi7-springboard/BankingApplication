import json
import os

# ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# print(ROOT_DIR)

class Service:
    global ROOT_DIR
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    # print(ROOT_DIR)
    def newLoanApplication(self):
        n = input("Enter CustomerId, Income, No.of dependants, Employer, Purpose of Loan: ")
        self.lst = [int(x) if x.isdigit() else x.strip() for x in n.split(',')]
        # print(self.lst)
        return self.lst

    def savingToJsonFile(self, data):
        # print("First element from Customer loan input data is: ", data[0])
        inputDict = {}
        inputDict[data[0]] = data
        # print(inputDict)
        # print(ROOT_DIR)
        serviceDataPath = os.path.join(ROOT_DIR, 'JsonDataFIles/serviceData.json')
        # print(serviceDataPath)
        with open(serviceDataPath, 'w') as f:
            json.dump(inputDict, f)
        print("\n-------Your application is being reviewed!!!--------\n")









if __name__ == '__main__':
    service = Service()
    inputData = service.newLoanApplication()
    service.savingToJsonFile(inputData)