from pprint import pprint
from Handlers import combinedHandler
from ProjectData import Constants

cb = combinedHandler.CombinedHandler(Constants.DATABASE_SHARED, Constants.BOT_TOKEN)

while True:
    cb.handleUpdates()
    _bindingKey = 'HENK'
    _regKey = Constants.CODE_HEADER_REGISTER + _bindingKey
    _result = cb.checkForRegistrationKeyInLoggedUpdates(_regKey)

    print(_result)

    if _result:
        cb.registerChatIdToUserViaRegKey(_bindingKey, _result)
