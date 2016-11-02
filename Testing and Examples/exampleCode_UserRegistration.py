#Example code to explain how our telegramHandler works
import time
from pprint import pprint

from Handlers import telegramHandler, DatabaseHandler

#constants
BOT_TOKEN = '166998703:AAGvk0No3abHbGc9LpUpJko7WTx1DR9jURY' #Access token to communicate with the API

HEADER_REGISTER = 'REGISTER:'
HEADER_IDENTIFY = 'C0D3:'

FAKE_DATABASE = 'fake.db'
FAKE_TABLE = 'fake'

currentUpdateId = 0 #starting point, this'll change with the first update received

#create a TelegramHandler object
tHandler = telegramHandler.TelegramHandler(BOT_TOKEN, currentUpdateId)

#create a databasehandler
myDB = DatabaseHandler.DatabaseHandler(FAKE_DATABASE)

#create a table in the new Database
myDB.runQuery('''
CREATE TABLE IF NOT EXISTS fake
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        chat_id INTEGER NOT NULL UNIQUE,
        temp_key TEXT
    )
''')


loopIsRunning = True

identificationDict = {}

#start our main loop
while loopIsRunning:

    #check if there are any updates available
    if not tHandler.hasNewUpdates():
        time.sleep(1)
        continue #skip this cycle

    #request new updates
    newUpdates = tHandler.getNewUpdates() #this code will either return all buffered updates, if there are no updates, it will wait for the next update

    # check if there were any new updates returned
    if not len(newUpdates) > 0: # IF len(newUpdates) is equal to zero, it means there were no new updates returned
        continue # skip this iteration if there are no new updates

    #handle each new update
    for update in newUpdates:
        # first we should check if the text in the update is usefull to us
        # there are two types op updates
        # 1. A new user registers to our bot
        # 2. An exicsting user enters a pincode to verify his identity

        pprint(update)

        #extrax=ct the actual message from the update data
        messageText = update['message']['text']

        # nr 1: The received message must start with 'REGISTER:'
        if messageText.startswith(HEADER_REGISTER):
            #extract register code
            registerCode = messageText.split(':')[1] #We need the substring starting after the ':'

            newItem = {
                'name': '?',
                'chat_id': update['message']['chat']['id'],
                'temp_key': registerCode
            }

            #add the new registerer to our 'database'
            result = myDB.insertNewItem(newItem, FAKE_TABLE)

            print(result)

        # nr 2: The received message must start with 'C0D3:'
        elif messageText.startswith(HEADER_IDENTIFY):
            #extract the identification code
            IDCode = messageText.split(':')[1] #We need the substring starting after the ':'

            #add the new identifiaction to our identificationList
            identificationDict.update({'chat_id': update['update_id'], 'code':IDCode})

        #lazy way to terminate the loop - DO NOT IMPLEMENT THIS!
        elif messageText.startswith('SHUTDOWN'):
            loopIsRunning = False

        else:
            #for now we will not precess anything we don't recognize
            pass

        if tHandler.current_response < update['update_id']:
            tHandler.current_response = update['update_id']

    #We now have receveived all new updates and handled them thusfar.
    #Now we should use our indexed updates.

    print(myDB.showTableContents(FAKE_TABLE))

    #let's, just for fun, send all unregistered users an update to remind them to register
    sql = "SELECT * FROM fake WHERE name = '?'"
    result = myDB.runQuery(sql)

    for unregisteredUser in result:
        #Define the user
        _recipient = unregisteredUser[2] #Ugly, Hard Coded position in the tuple

        #Define the message to send
        _message = "Hi, you have not yet finished your registration. Please do this A.S.A.P.!"

        #try to send the message and save the result (Either an error or a full messageDict)
        _result = tHandler.sendMessageToUser(_recipient, _message)

        print('RESULT: {}'.format(_result))


    #Save the database to ensure no data is lost on a sudden crash
    myDB.saveDatabase()

    #avoid updating too quickly!
    print('sleepy time... ')

    sleepTimeSeconds = 5
    time.sleep(sleepTimeSeconds) #sleep for 5 seconds
    print('waking up after {} seconds...'.format(sleepTimeSeconds))


#This will ensure that all data is saved to the Database
del myDB
