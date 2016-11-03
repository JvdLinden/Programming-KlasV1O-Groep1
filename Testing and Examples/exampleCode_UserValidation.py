from userValidator import UserValidator
from ProjectData import Constants
from Handlers import databaseHandler, telegramHandler, combinedHandler

#create a DatabaseHandler object
myCH = combinedHandler.CombinedHandler(database=Constants.DATABASE_MASK, telegram=Constants.BOT_TOKEN)
# Create a validator object (the UserValidator-object requires a DatabaseHandler)
myObject = UserValidator(myCH)

# when the validator object is done running, retrieve the value.
newValue = myObject.getValue()

# print Value
print(newValue)
