from Helpers.ConfigReader import ReadConfiguration 

conf = ReadConfiguration()
baseUri = conf.getGlobalValueFromConfig('BaseUrl')

forename = conf.getContactFormValue('Forename')
fornameErrorMessage = conf.getContactFormValue('ForenameErrorMessage')
email = conf.getContactFormValue('Email')
emailErrorMessage = conf.getContactFormValue('EmailErrorMessage')
message = conf.getContactFormValue('MessageText')
messageErrorMessage = conf.getContactFormValue('MessageErrorMessage')
successfulMessage = conf.getContactFormValue('SuccessMessage').replace('{Forename}',forename)

shopItems = conf.getShopValues()
