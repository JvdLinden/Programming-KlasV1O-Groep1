from ProjectData import Constants
from Handlers import telegramHandler, databaseHandler

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
        # zorgen dat de code stop wanneer er niets te verwerken valt
        if self.telegram.hasNewUpdates():
            updates = self.telegram.getNewUpdates()

            for update in updates:
                self.storeUpdate(update)

    def storeUpdate(self, update):

        if not self.database.runQuery("SELECT * FROM {} WHERE update_id = {} ".format(Constants.TABLE_USERS, update['update_id'])):
            message = update['message']
            chat = message['chat']
            from_user = message['from']

            _dict = {
                'name': from_user['first_name'] + '' + from_user['last_name'],
                'chat_id': chat['id'],
                'date': message['date'],
                'user_id': from_user['id'],
                'text': message['text'],
                'update_id': update['update_id'],
            }

            self.telegram.registerUpdateID(update['update_id'])

            self.database.insertNewItem(_dict, Constants.TABLE_UPDATES)
            self.database.saveDatabase()

    def registerNewUser(self, userData):
        """This functions registers a new user, with the given *userData*
        userData should be a dict containing the following:
            dict = {
                'name': <username>,
                'street': <street>,
                'house_nr':<house_nr>,
                'house_nr_ext':<house_nr_ext>',
                'phone_nr':<phone_nr>,
                'reg_key':<unique registration key>,
                'bike_key':<unique bike identificaiton key>,
            }

        :param userData: required userdata
        :return: True (succes, False (failure)
        """
        _result = self.database.insertNewItem(userData, Constants.TABLE_USERS)
        return _result
