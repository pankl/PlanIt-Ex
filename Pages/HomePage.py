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
        self.click(HomePageLocators.ContactButtonLocator)
        logger.debug("Clicked on contact button")

    def clickShopButton(self):
        self.click(HomePageLocators.ShopButtonLocator)
        logger.debug("Clicked on shop button")