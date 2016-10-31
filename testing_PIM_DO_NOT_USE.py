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
myTable = 'testing'

myDB = DatabaseHandler.DatabaseHandler('test.db')

myDB.registerNewUser(myDict)
print(myDB.showTableContents(myTable))

del myDB
