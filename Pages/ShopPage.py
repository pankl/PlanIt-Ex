from Pages.BasePage import BasePage
from Resources.ShopPageLocators import ShopPageLocators
from Helpers.Constants import * 
from Helpers.MyLogger import getmylogger
import time

logger = getmylogger(__name__)

class ShopPage(BasePage):
    def __init__(self, driver) :
        super().__init__(driver)

    def buyItem(self,item):
        (itemName, qty) = item
        for i in range(int(qty)):
            self.clickBuyButton(itemName)
        time.sleep(3)
    
    def getItemPrice(self, item):
        return self.get_text(ShopPageLocators.ItemPriceText, item[0])

    def clickBuyButton(self,itemName):
        try:
            self.click(ShopPageLocators.BuyItemButton, itemName)
            logger.debug(f'Clicked on {itemName} buy button')
        except:
            logger.error(f'Failed to locate item {itemName}, used {ShopPageLocators.BuyItem} locator')
            raise