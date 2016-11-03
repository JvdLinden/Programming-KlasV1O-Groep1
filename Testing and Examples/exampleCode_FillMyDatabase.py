from pprint import pprint
from Handlers import telegramHandler, databaseHandler
from ProjectData import Constants

myTelegramHandler = telegramHandler.TelegramHandler(Constants.BOT_TOKEN, 0)
myDatabaseHandler = databaseHandler.DatabaseHandler(Constants.DATABASE_SHARED)

TABLE_USERS = 'users'
REGISTRATION_HEADER = 'REG:'
CREATION_CODE = "CRT:"
myDatabaseHandler.runQuery('DROP TABLE {}'.format(TABLE_USERS))

myDatabaseHandler.runQuery('''
CREATE TABLE IF NOT EXISTS {}
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        chat_id INTEGER,
        temp_key TEXT
    )
'''.format(TABLE_USERS))

loopIsRunning = True

newItem = {
    'name': 'Pim',
    'temp_key': 'AABB',
    'chat_id': 1001,
}

result = myDatabaseHandler.insertNewItem(newItem, TABLE_USERS)



print(result)
print(myDatabaseHandler.showTableContents(TABLE_USERS))

while loopIsRunning:
     #check if there are any updates available
    if not myTelegramHandler.hasNewUpdates():
        continue #skip this cycle

    updates = myTelegramHandler.getNewUpdates()

    if not len(updates) > 0:
        continue

    for update in updates:
        pprint(update)

        messageText = update['message']['text']

        myTelegramHandler.registerUpdateID(update['update_id'])

        if messageText.startswith(REGISTRATION_HEADER):
            _key = messageText.strip(REGISTRATION_HEADER).split()[0] # First element after the registration-tag
            _result = myDatabaseHandler.runQuery("SELECT id FROM {} WHERE temp_key = '{}'".format(TABLE_USERS, _key))

            if not isinstance(_result, str):
                _sql = "UPDATE {} SET chat_id = {}, temp_key = '' WHERE temp_key = '{}'".format(TABLE_USERS, update['message']['chat']['id'], _key)
                _result = myDatabaseHandler.runQuery(_sql)

        print(myDatabaseHandler.showTableContents(TABLE_USERS))

        myDatabaseHandler.saveDatabase()
