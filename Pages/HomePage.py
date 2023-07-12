from Pages.BasePage import BasePage
from Resources.HomePageLocators import HomePageLocators
from Helpers.Constants import * 
from Helpers.MyLogger import getmylogger

logger = getmylogger(__name__)

class HomePage(BasePage):
    def __init__(self, driver) :
        super().__init__(driver)
        

    def navigateToHomePage(self):
        self.wait_for_element(HomePageLocators.ContactButtonLocator)


    def clickContactButton(self):
        try:
            self.click(HomePageLocators.ContactButtonLocator)
            logger.debug("Clicked on contact button")
        except:
            logger.error(f'Failed to locate contact button, used {HomePageLocators.ContactButtonLocator} locator')
            raise

    def clickShopButton(self):
        try:
            self.click(HomePageLocators.ShopButtonLocator)
            logger.debug("Clicked on shop button")
        except:
            logger.error(f'Failed to locate shop button, used {HomePageLocators.ShopButtonLocator} locator')
            raise
        
    def clickCartButton(self):
        try:
            self.click(HomePageLocators.CartButtonLocator)
            logger.debug("Clicked on cart button")
        except:
            logger.error(f'Failed to locate cart button, used {HomePageLocators.CartButtonLocator} locator')
            raise