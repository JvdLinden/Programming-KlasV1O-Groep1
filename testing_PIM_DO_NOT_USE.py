# import DatabaseHandler
#
# # testing Dictionary
# myDict = {
#     'name':'naam1',
#     'street':'straat2',
#     'house_number':'11',
#     'house_number_extra':'a1',
#     'city':'stad1',
#     'postal_code':'1243DB',
#     'phone_number':12323678
# }
#
# #testing Table
# myTable = 'users'
#
# myDB = DatabaseHandler.DatabaseHandler('test.db')
#
# myDB.runQuery('''
# CREATE TABLE IF NOT EXISTS users
#     (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         street TEXT NOT NULL,
#         house_number INT NOT NULL,
#         house_number_extra TEXT,
#         city TEXT NOT NULL,
#         postal_code TEXT NOT NULL,
#         phone_number INTEGER NOT NULL
#     )
# ''')
#
# result = myDB.insertNewItem(myDict,myTable)
#
# print(result)
#
# myDict = {
#     'neem':'naam1',
#     'street':'straat2',
#     'house_number':'11',
#     'house_number_extra':'a1',
#     'city':'stad1',
#     'postal_code':'1243DB',
#     'phone_number':12323678
# }
# myDB.insertNewItem(myDict,myTable)
# print(myDB.showTableContents(myTable))
#
# del myDB
#
#
#

#TELEGRAM TESTSITE
import telegramHandler

token = '166998703:AAGvk0No3abHbGc9LpUpJko7WTx1DR9jURY'

myTelegramHandler = telegramHandler.TelegramHandler(token, 0)

while True:
    newUpdate = myTelegramHandler.getNextUpdate()
    if len(newUpdate) > 0:
        dictList = myTelegramHandler.handleUpdates(newUpdate)

        #Verwerk nieuwe codes
        for item in dictList:
            for key in item:
                print('{}{}'.format(key, item[key]), end=' ,')

            print()
            #REGISTER CODE SOMEWHERE

            myTelegramHandler.sendMessageToUser(item['id'], item['code'])
