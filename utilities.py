import json
from constants import USER_FILE_PATH


class Utilities:


    def savingToJsonFile(self, data, filePath):
        # print("First element from Customer loan input data is: ", data[0])
        # print(filePath)
        inputDict = {}
        inputDict[data[0]] = data
        # print(inputDict)
        # print(ROOT_DIR)
        # serviceDataPath = os.path.join(ROOT_DIR, 'JsonDataFIles/serviceData.json')
        # print(serviceDataPath)
        with open(filePath, 'w') as f:
            json.dump(inputDict, f)




# if __name__ == '__main__':
#     utilities = Utilities()
    # utilities.savingToJsonFile("Kiran, C, kc@gmail.com, kc, kcp, 12321323, 1989-04-10, 10Corporate, 22334", USER_FILE_PATH)