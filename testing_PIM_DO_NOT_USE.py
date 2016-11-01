import DatabaseHandler

# testing Dictionary
myDict = {
    'name':'naam1',
    'street':'straat2',
    'house_number':'11',
    'house_number_extra':'a1',
    'city':'stad1',
    'postal_code':'1243DB',
    'phone_number':12323678
}

#testing Table
myTable = 'users'

myDB = DatabaseHandler.DatabaseHandler('test.db')

myDB.runQuery('''
CREATE TABLE IF NOT EXISTS users
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        street TEXT NOT NULL,
        house_number INT NOT NULL,
        house_number_extra TEXT,
        city TEXT NOT NULL,
        postal_code TEXT NOT NULL,
        phone_number INTEGER NOT NULL
    )
''')

result = myDB.insertNewItem(myDict,myTable)

print(result)

myDict = {
    'neem':'naam1',
    'street':'straat2',
    'house_number':'11',
    'house_number_extra':'a1',
    'city':'stad1',
    'postal_code':'1243DB',
    'phone_number':12323678
}
myDB.insertNewItem(myDict,myTable)
print(myDB.showTableContents(myTable))

del myDB



