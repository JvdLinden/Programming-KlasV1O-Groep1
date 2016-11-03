from pprint import pprint
from Handlers import combinedHandler
from ProjectData import Constants

cb = combinedHandler.CombinedHandler(Constants.DATABASE_SHARED, Constants.BOT_TOKEN)

print(cb.retrievePersonalData('ABE'))
