import sqlite3

class DatabaseHandler(object):

    def __init__(self, databaseFile):
        """Return a DatabaseHandler wich represents a connection
        to the given database *databaseFile* """
        self.databaseFile = databaseFile
        self.connection = sqlite3.connect(databaseFile)
        self.cursor = self.connection.cursor()

        # Onderstaande gebruiken voor een NIEUWE TABEL
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS testing
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            street TEXT NOT NULL,
            house_number INT NOT NULL,
            house_number_extra TEXT,
            city TEXT NOT NULL,
            postal_code TEXT NOT NULL,
            phone_number INTEGER NOT NULL
        )''')

    def __del__(self):
        """This destructor ensures the database connection is properly closed"""
        self.connection.commit()
        self.connection.close()

    def createInsertQuery(self, inDict, table):
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

    def registerNewUser(self, userDataDict):
        myTable = 'testing'
        myQuery = self.createInsertQuery(userDataDict, myTable)

        #DEBUG: debuggingLine
        print('DEBUG: '+myQuery)

        self.cursor.execute(myQuery)

    def showTableContents(self, table):
        self.cursor.execute("SELECT * FROM {}".format(table))
        return self.cursor.fetchall()
