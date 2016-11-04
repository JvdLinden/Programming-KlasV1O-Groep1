from ProjectData import Constants, Messages
from Handlers import telegramHandler, databaseHandler
import time

class CombinedHandler(object):
    """
        This class van handle all database and telegram operations
    """
    def __init__(self, database, telegram):
        self.database = databaseHandler.DatabaseHandler(database)
        self.telegram = telegramHandler.TelegramHandler(telegram, 0)

    def handleUpdates(self):
        """Verwerkt nieuwe updates in de database.

        :param database: de database waarin de updates moeten worden opgeslagen
        :return: nothing
        """
        # only handle updates if there are any
        if self.telegram.hasNewUpdates():
            updates = self.telegram.getNewUpdates()

            for update in updates:
                self.__storeUpdate(update)

    def __storeUpdate(self, update):
        """Private function to store all relevant data of an update into our database

        :param update: the update to store
        :return: the result of the insert query
        """

        # check for duplicates via de update_id number
        _sql = "SELECT * FROM {} WHERE update_id = {} ".format(Constants.TABLE_UPDATES, update['update_id'])
        _result = self.database.runQuery(_sql)

        if len(_result) == 0:
            # if there are no results, insert a new row into the database
            message = update['message']
            chat = message['chat']
            from_user = message['from']

            # create a dict, the databaseHandler can convert a dict into an sql-Insert query
            _dict = {
                'name': from_user['first_name'] + '' + from_user['last_name'],
                'chat_id': chat['id'],
                'date': message['date'],
                'user_id': from_user['id'],
                'text': message['text'],
                'update_id': update['update_id'],
            }

            #register the new updateId to the telegramHandler object
            self.telegram.registerUpdateID(update['update_id'])

            _result = self.database.insertNewItem(_dict, Constants.TABLE_UPDATES)
            self.database.saveDatabase()

    def registerChatIdToUserViaRegKey(self, regKey, chatID):
        """DO NOT USE THIS METHOD WITH UNVERIFIED DATA!
        This method binds a chat id to a user via the user's *regKey*

        :param regKey: the registration key of the user
        :param chatID: the chatID of the user
        :return: nothing
        """
        _sql = "UPDATE {} SET chat_id = {}, reg_key = '' WHERE reg_key = '{}'".format(Constants.TABLE_USERS, chatID, regKey)
        _result = self.database.runQuery(_sql)
        self.database.saveDatabase()
        return _result

    def getChatIdViaRegistrationKeyInLoggedUpdates(self, registrationKey):
        """Function to check if a certain registrationKey has been used yet.

        :param registrationKey:
        :return: the chat_id linked to this registrationKey, False if no key was found
        """
        _result = self.database.runQuery("SELECT chat_id FROM {} WHERE text = '{}' AND used = 0".format(Constants.TABLE_UPDATES, registrationKey))

        if _result:
            # list the update from which we retrieved the data as 'used' in the database.
            self.database.runQuery("UPDATE {} SET used = 1 WHERE text = '{}'".format(Constants.TABLE_UPDATES, registrationKey))

            # sqlite database returns a list with tuples containing row data (tuples in list).
            #  we only expect 1 answer so we need the item on position 0 of the first list and position 0 of the tuple in said list
            return _result[0][0]
        else:
            return False

    def checkIfRegistrationKeyExistsInUpdates(self, key):
        """This function check if the geiven *key* has been newly - entered by  a user

        :param key: the key to find
        :return: True if found, False if not
        """
        if self.database.runQuery("SELECT chat_id FROM {} WHERE text = '{}' AND used = 0".format(Constants.TABLE_UPDATES, key)):
            return True
        return False

    def retrievePersonalData(self, bikeKey):
        """Retreive the presonal data for a user via het special identification key *bikeKey*

        :param bikeKey: the special
        :return: the data in a tuple
        """
        _sql = "SELECT * FROM {} WHERE bike_key LIKE '%{}%'".format(Constants.TABLE_USERS, bikeKey)
        _result = self.database.runQuery(_sql)
        if _result:
            return _result
        else:
            return False

    def storeBike(self, bike_key):
        # check if bike isn't already stalled
        _sql = "SELECT * FROM {} WHERE bike_key = '{}' and retrieved = 0".format(Constants.TABLE_ENTRIES, bike_key)
        _result = self.database.runQuery(_sql)
        # actual check
        if _result:
            return 'Uw fiets is al aanwezig in onze stalling'
        else:
            _result = self.database.insertNewItem(
                {'bike_key': bike_key, 'date_stored': str(time.strftime('%x %X'))},
                Constants.TABLE_ENTRIES
            )
            _user = self.database.getChatIDFromPersonalCode(bike_key)
            self.telegram.sendMessageToUser(_user, Messages.FIETS_GESTALD)
            return 'U heeft uw fiets gestald'

    def retrieveBike(self, bike_key):
        _sql = "SELECT * FROM {} WHERE bike_key = '{}' and retrieved=0".format(Constants.TABLE_ENTRIES, bike_key)
        _result = self.database.runQuery(_sql)
        self.database.saveDatabase()

        if len(_result) > 0:
            _sql = "UPDATE {} SET retrieved=1, date_retrieved='{}' WHERE bike_key = '{}' and retrieved=0".format(Constants.TABLE_ENTRIES,time.strftime('%x %X'),  bike_key)
            _result = self.database.runQuery(_sql)
            self.database.saveDatabase()
            self.sendBikeRetreivedMessage(bike_key)
            return True
        else:
            return False

    def sendBikeRetreivedMessage(self, bike_key):
        _user = self.database.getChatIDFromPersonalCode(bike_key)
        self.telegram.sendMessageToUser(_user, Messages.FIETS_OPGEHAALD)

    def registerNewUser(self, userData):
        """This functions registers a new user, with the given *userData*
        userData should be a dict containing the following:
            dict = {
                'name': <username>,
                'street': <street>,
                'house_nr':<house_nr>,
                'postal_code':<house_nr_ext>',
                'phone_nr':<phone_nr>,
                'reg_key':<unique registration key>,
                'bike_key':<unique bike identificaiton key>,
            }

        :param userData: required user data
        :return: True (succes), False (failure)
        """
        _result = self.database.insertNewItem(userData, Constants.TABLE_USERS)
        self.database.saveDatabase()
        return _result
