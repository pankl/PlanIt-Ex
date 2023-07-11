from Pages.BasePage import BasePage
from Resources.ContactPageLocators import ContactPageLocators
from Helpers.Constants import * 
from Helpers.MyLogger import getmylogger
import time

logger = getmylogger(__name__)

class ContactPage(BasePage):
    def __init__(self, driver) :
        super().__init__(driver)


    def clickSubmitButton(self):
        self.click(ContactPageLocators.SubmitButton)
        logger.debug("Clicked on submit button")

    def inputForNameText(self,text):
        logger.debug("Typing {} in Forename field".format(text))
        self.wait_for_element(ContactPageLocators.ForeNameInput)
        self.click(ContactPageLocators.ForeNameInput)
        self.enter_text(ContactPageLocators.ForeNameInput,text)

    def getForeNameErrorMessage(self):
        logger.info("Awaiting error message text for Forname")
        return self.get_text(ContactPageLocators.ForeNameErrorMessage)
    
    def inputEmailText(self,text):
        logger.debug("Typing {} in Email field".format(text))
        self.wait_for_element(ContactPageLocators.EmailInput)
        self.click(ContactPageLocators.EmailInput)
        self.enter_text(ContactPageLocators.EmailInput,text)
        
    def getEmailErrorMessage(self):
        logger.info("Awaiting error message text for Email")
        return self.get_text(ContactPageLocators.EmailErrorMessage)
    
    def inputMessageText(self,text):
        logger.debug("Typing {} in Message field".format(text))
        self.wait_for_element(ContactPageLocators.MessageInput)
        self.click(ContactPageLocators.MessageInput)
        self.enter_text(ContactPageLocators.MessageInput,text)
        
    def getMessageErrorMessage(self):
        logger.info("Awaiting error message text for Message")
        return self.get_text(ContactPageLocators.MessageErrorMessage)
    
    def getSuccessMessage(self):
        logger.info("Awaiting success message text for valid submission")
        self.wait_for_element_to_be_gone(ContactPageLocators.SubmitProgressBar)
        return self.get_text(ContactPageLocators.SuccessfulSubmissionMessage)