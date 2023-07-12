from Pages.BasePage import BasePage
from Resources.ShopPageLocators import ShopPageLocators
from Helpers.Constants import * 
from Helpers.MyLogger import getmylogger

logger = getmylogger(__name__)

class ShopPage(BasePage):
    def __init__(self, driver) :
        super().__init__(driver)

    def buyItem(self,item):
        (itemName, qty) = item
        for i in range(int(qty)):
            self._clickBuyButton(itemName)
    
    def getItemPrice(self, item):
        try:
            logger.debug(f'Awaiting to get item price for {item[0]}')
            return self.get_text(ShopPageLocators.ItemPriceText, item[0])
        except:
            logger.error(f'Failed to locate item {item[0]}, used {ShopPageLocators.ItemPriceText} locator')
            raise

    def _clickBuyButton(self,itemName):
        try:
            self.click(ShopPageLocators.BuyItemButton, itemName)
            logger.debug(f'Clicked on {itemName} buy button')
        except:
            logger.error(f'Failed to locate item {itemName}, used {ShopPageLocators.BuyItem} locator')
            raise