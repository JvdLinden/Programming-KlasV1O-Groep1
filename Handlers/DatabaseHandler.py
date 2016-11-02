import sqlite3

TABLE_USERS = 'users'
TABLE_ENTRIES = 'entries'

class DatabaseHandler(object):
    """This is the DatabaseHandler class.
    This classes'sole purpose is to handle a database connection to a sqlite3 database.

    """

    def __init__(self, databaseFile):
        """Create a DatabaseHandler which handles a connection to the given database *databaseFile*

        :param databaseFile: the database file to read/use
        """
        self.databaseFile = databaseFile
        self.connection = sqlite3.connect(databaseFile)
        self.cursor = self.connection.cursor()

    def __del__(self):
        """This destructor ensures that the database connection is properly closed

        """
        self.connection.commit()
        self.connection.close()

    def __createInsertQuery(self, inDict, table):
        """This private function generates an insert query based on a dict with values.

        :param inDict: Dictionary with values related to id's in the given *table*
        :param table: the table to insert a row into
        :return: the INSERT INTO query
        """
        _checkedDict = {}

        for key in inDict.keys():
            _value = inDict[key]
            if _value:
                if isinstance(_value, str):
                    _value = "'{}'".format(_value)
                else:
                    _value = str(_value)
                _checkedDict.update({key: _value})

        return "INSERT INTO {0} ({1}) VALUES ({2})".format(table, ','.join(_checkedDict.keys()), ','.join(_checkedDict.values()))

    def saveDatabase(self):
        """This function allows another part of the application to save all buffered data.

        :return: None
        """
        self.connection.commit()

    def runQuery(self, sql):
        """This function safely executes sql-queries

        :param sql: The query that has to be executed
        :return: either the errormessage or the result of fetchAll
        """
        try:
            self.cursor.execute(sql)
        except Exception as e:
            return str(e.args)
        return self.cursor.fetchall()

    def insertNewItem(self, dataDict, table):
        """This function can insert a new row into a given *table*.

        :param dataDict: A dictionary with table id's and their respective values
        :param table: The table the data has to be inserted into
        :return: the result of the executed query
        """
        myQuery = self.__createInsertQuery(dataDict, table)

        #Execute query and fetch result
        _result = self.runQuery(myQuery)

        #return the result of the excuted query
        return _result

    def showTableContents(self, table):
        """"Returns ALL contents from a Table

        """
        _result = self.runQuery("SELECT * FROM {}".format(table))

        return _result

    def getChatIDFromPersonalCode(self, personalCode):
        _sql = "SELECT telegram_chat_id FROM users WHERE personal_code = '{}'".format(personalCode)
        _result = self.runQuery(_sql)
