from Validation.userValidator import UserValidator
from ProjectData import constants
from Handlers import combinedHandler

#create a DatabaseHandler object
myCH = combinedHandler.CombinedHandler(database=constants.DATABASE_MASK, telegram=constants.BOT_TOKEN)
# Create a validator object (the UserValidator-object requires a DatabaseHandler)
myObject = UserValidator(myCH)

# when the validator object is done running, retrieve the value.
newValue = myObject.getValue()

# print Value
print(newValue)
