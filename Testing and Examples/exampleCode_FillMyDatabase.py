from pprint import pprint
from Handlers import combinedHandler
from ProjectData import constants

cb = combinedHandler.CombinedHandler(constants.DATABASE_SHARED, constants.BOT_TOKEN)

print(cb.retrievePersonalData('ABE'))
