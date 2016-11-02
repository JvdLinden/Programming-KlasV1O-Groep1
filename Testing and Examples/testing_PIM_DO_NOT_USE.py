from userValidator import UserValidator
from ProjectData import Constants
from Handlers import databaseHandler

myDB = databaseHandler.DatabaseHandler(Constants.DATABASE_MASK)

# Create a validator object
myObject = UserValidator(myDB)

# when the validator object is done running, retrieve the value.
newValue = myObject.getValue()

# print Value
print(newValue)
