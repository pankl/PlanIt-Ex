from Pages.BasePage import BasePage
from Resources.ContactPageLocators import ContactPageLocators
from Helpers.Constants import * 
from Helpers.MyLogger import getmylogger

logger = getmylogger(__name__)

class ContactPage(BasePage):
    def __init__(self, driver) :
        super().__init__(driver)


    def clickSubmitButton(self):
        self.click(ContactPageLocators.SubmitButton)
        logger.debug("Clicked on submit button")

    def inputForNameText(self,text):
        self.fillInTextInInputField(text, ContactPageLocators.ForeNameInput)
    
    def inputEmailText(self,text):
        self.fillInTextInInputField(text, ContactPageLocators.EmailInput)
    
    def inputMessageText(self,text):
        self.fillInTextInInputField(text, ContactPageLocators.MessageInput)
        
    def getSuccessMessage(self):
        try:
            logger.info("Awaiting success message text for valid submission")
            self.wait_for_element_to_be_gone(ContactPageLocators.SubmitProgressBar)
            return self.get_text(ContactPageLocators.SuccessfulSubmissionMessage)
        except:
            logger.error(f'Failed to locate success message, used {ContactPageLocators.SuccessfulSubmissionMessage} locator')
            raise

    
    def getErrorMessage(self,field):
        try:
            logger.info(f"Awaiting error message text for {field}")
            return self.get_text(ContactPageLocators.ErrorMessage, field.lower())
        except:
            logger.error(f'Failed to locate {field}, used {ContactPageLocators.ErrorMessage} locator')
            raise
            
    
    def fillInTextInInputField(self,text,locator):
        try:
            logger.debug(f"Typing {text} in Message field")
            self.wait_for_element(locator)
            self.click(locator)
            self.enter_text(locator,text)
        except:
            logger.error(f'Failed to type into text input, used {locator} locator')
            raise