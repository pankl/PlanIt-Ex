from Pages.BasePage import BasePage
from Resources.CartPageLocators import CartPageLocators
from Helpers.Constants import * 
from Helpers.MyLogger import getmylogger

logger = getmylogger(__name__)

class CartPage(BasePage):
    def __init__(self, driver) :
        super().__init__(driver)

    def getSubTotal(self):
        try:
            logger.info('Awaiting total text in cart')
            return self.get_text(CartPageLocators.subTotalText)
        except:
            logger.error(f'Failed to locate total text, used {CartPageLocators.subTotalText} locator')
            raise
    
    def getCartRow(self, itemName):
        try:
            logger.info('Awaiting items in cart')
            self.rows = self.get_table_rows(CartPageLocators.cartTableRows)
            for row in self.rows:
                if (itemName in row.text):
                    return tuple(row.text.split(' $')[1:])
        except:
            logger.error(f'Failed to items in cart, used {CartPageLocators.cartTableRows} locator')
            raise