import pymysql
import datetime
from mysql.connector import connect, Error


# Connection class which returns an instance of mysql connection

class MySQLConnector:
    dbUsername = 'root'
    dbpassword = 'rootadmin'
    schema_name = 'Banking_System'
    host = 'localhost'
    print(dbUsername)

    def __init__(self):
        pass

    ######################################################################################################
    # QUERY EXECUTION

    @staticmethod
    def connect_to_db():
        db = pymysql.connect(host=MySQLConnector.host,
                             user=MySQLConnector.dbUsername,
                             password=MySQLConnector.dbpassword,
                             db=MySQLConnector.schema_name)
        print(db)
        print("Successfully Connected to database !!!")
        return db

    def executeWriterQuery(self, query):
        db = self.connector.connectToDbWriter()
        cursor = db.cursor()
        cursor.execute(query)
        db.commit()
        results = cursor.fetchall()
        cursor.close()
        db.close()
        return results

    def executeWriterQueryForeignKey(self, query):
        db = self.connector.connectToDbWriter(MySQLConnector.schema_name)
        cursor = db.cursor()
        cursor.execute("SET FOREIGN_KEY_CHECKS=0")
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.execute("SET FOREIGN_KEY_CHECKS=1")
        db.commit()
        cursor.close()
        db.close()
        return results



#####################################################################################################
# QUERY EXECUTION
    def executeQuery(self, query):
        db = self.connect_to_db()
        cursor = db.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        db.close()
        return result



# ######################################################################################################
# schema_name arg is compulsory because it is used in query directly


    def getMySQLColumnNames(self, table_name):
        query = """SELECT COLUMN_NAME
                   FROM INFORMATION_SCHEMA.COLUMNS
                   WHERE TABLE_SCHEMA = '{}' AND TABLE_NAME = '{}'
                   ORDER BY ORDINAL_POSITION""".format(MySQLConnector.schema_name, table_name)
        print("Query from getMySQLColNames:",query)
        column_names = self.executeQuery(query)
        column_list = list(map(list, column_names))
        flat_list = [item for sublist in column_list for item in sublist]
        res = [flat_list[i] for i in range(1, len(flat_list) - 2)]
        # res = flat_list[1::len(flat_list)-2]
        print("Eleminating ID and last 2 records", res)
        # print(type(flat_list[0]))
        # print(flat_list)
        return res


    def convertListToString(self, sentList):
        result = ""
        for row in sentList:
            result += row + ","
        result = result[:-1]
        return result

    # used for queries only since it replaces ' by ''
    def convertListToQuotedString(self, sentList):
        result = ""
        for row in sentList:
            result += self.checkValue(row) + ","
        result = result[:-1]
        return result

    def checkValue(self, value):
        if type(value)  == type("hello"):
            return "'{}'".format(value.replace("'","''"))      #repr(value)
        elif type(value) == type(None):
            return '{}'.format("NULL")#"''"
        elif type(value) == type(7):
            return '{}'.format(value) #str(value)
        elif type(value) == type(7.9):
            return '{}'.format(value) #str(value)
        elif type(value) == type(datetime.datetime(2019, 1, 3, 15, 27, 18)):
            return "'{}'".format(value) #"'" +str(value)+ "'"
        else:
            print("Could not find" + str(type(value)) + " for value " +str(value))
            return "'{}'".format(value) #str(value)


    def insertRows(self, table_name, columns, row_data):
        # columnList = [k for k,v in row_data.items()]
        columnString = self.convertListToString(columns)
        print("DB Column String",columnString)
        # valueList = [v for k,v in row_data.items()]
        valueString = self.convertListToQuotedString(row_data)
        query = "INSERT INTO `{}`({}) VALUES ({})".format(table_name, columnString, valueString)
        print("Printing query from insertRows method: ",query)
        self.executeWriterQuery(query)







if __name__ == '__main__':
    mysql = MySQLConnector()
    mysql.connect_to_db()
    mysql.getMySQLColumnNames('USER')