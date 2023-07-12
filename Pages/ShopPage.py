from Pages.BasePage import BasePage
from Resources.ShopPageLocators import ShopPageLocators
from Helpers.Constants import * 
from Helpers.MyLogger import getmylogger

logger = getmylogger(__name__)

class ShopPage(BasePage):
    def __init__(self, driver) :
        super().__init__(driver)

    def buyItem(self,item):
        
        for i in range(item.itemQty):
            self._clickBuyButton(item.itemName)
    
    def getItemPrice(self, item):
        try:
            logger.debug(f'Awaiting to get item price for {item.itemName}')
            return self.get_text(ShopPageLocators.ItemPriceText, item.itemName)
        except:
            logger.error(f'Failed to locate item {item.itemName}, used {ShopPageLocators.ItemPriceText} locator')
            raise

    def _clickBuyButton(self,itemName):
        try:
            self.click(ShopPageLocators.BuyItemButton, itemName)
            logger.debug(f'Clicked on {itemName} buy button')
        except:
            logger.error(f'Failed to locate item {itemName}, used {ShopPageLocators.BuyItem} locator')
            raise