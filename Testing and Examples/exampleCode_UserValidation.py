from userValidator import UserValidator
from ProjectData import Constants
from Handlers import databaseHandler

#create a DatabaseHandler object
myDB = databaseHandler.DatabaseHandler(Constants.DATABASE_MASK)

# Create a validator object (the UserValidator-object requires a DatabaseHandler)
myObject = UserValidator(myDB)

# when the validator object is done running, retrieve the value.
newValue = myObject.getValue()

#delete the objects after using! (doens't really matter though, Python wil handle this by itself
del myDB
del myObject

# print Value
print(newValue)
