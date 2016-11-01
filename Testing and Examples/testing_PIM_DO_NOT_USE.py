# import DatabaseHandler
#
# registerName = "Henkie33"
#
# #testing Table
# myTable = 'users'
#
# myDB = DatabaseHandler.DatabaseHandler('test.db')
#
# myDB.runQuery("DROP TABLE users")
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
#         phone_number INTEGER NOT NULL,
#         chat_id INTEGER NOT NULL UNIQUE
#     )
# ''')

#TELEGRAM TESTSITE
from Handlers import telegramHandler

#Private Bot Token
token = '166998703:AAGvk0No3abHbGc9LpUpJko7WTx1DR9jURY'

myTelegramHandler = telegramHandler.TelegramHandler(token, 0)

registerName = "Harold2"
registerCode ="AGD35ADS"
returnCode = ''

print('Registreer u met de volgende code: %s' % registerCode)
update_v = 946648556
running = True
while running:

    newUpdate = myTelegramHandler.getNextUpdate(update_v + 1)

    if not len(newUpdate) > 0:
        continue

    dictList = myTelegramHandler.handleUpdates(newUpdate)
    print(dictList)
    #Verwerk nieuwe codes
    item = dictList[0]

    update_v = item['uid']
    message = item['text']

    # for char in message:
    #     print('Chr: {}; No: {}; Rev: {}'.format(char, ord(char), chr(ord(char))))
    #returnCode = item['id']

    # REGISTER CODE SOMEWHERE
    if item['code'] == registerCode:
        _message = '*We* hebben [u](http://www.example.com/) geregisteerd, %s %c' % (registerName, chr(9989))
        myTelegramHandler.sendMessageToUser(chat_id=item['id'], message=_message)

#
# # testing Dictionary
# myDict = {
#     'name':registerName,
#     'street':'een zeker straatje',
#     'house_number':'11',
#     'house_number_extra':'a',
#     'city':'Utrecht',
#     'postal_code':'1243DB',
#     'phone_number':12323678,
#     'chat_id':returnCode
# }
#
# result = myDB.insertNewItem(myDict,myTable)
# print(myDB.showTableContents(myTable))
#
# #Lookup user
# sql = "SELECT * FROM {} WHERE name = '{}'".format(myTable, registerName)
# result = myDB.runQuery(sql)
# print(result)
#
# del myDB
