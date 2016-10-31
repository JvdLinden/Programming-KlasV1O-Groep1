import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()

# Onderstaande gebruiken voor een NIEUWE TABEL
cur.execute('''CREATE TABLE IF NOT EXISTS testing
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

myDict = {
    'name':'naam1',
    'street':'straat2',
    'house_number':'11',
    'house_number_extra':'a1',
    'city':'stad1',
    'postal_code':'1243DB',
    'phone_number':12323678
}
myTable = 'testing'

def createInsertQuery(inDict, table):
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

myQuery = createInsertQuery(myDict, myTable)

print(myQuery)


cur.execute(myQuery)

con.commit()

cur.execute("SELECT * FROM testing")

print(cur.fetchall())

con.close()
