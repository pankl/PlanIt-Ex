from Pages.BasePage import BasePage
from Resources.CartPageLocators import CartPageLocators
from Helpers.Constants import * 
from Helpers.MyLogger import getmylogger
import time

logger = getmylogger(__name__)

class CartPage(BasePage):
    def __init__(self, driver) :
        super().__init__(driver)

    def getSubTotal(self):
         return self.get_text(CartPageLocators.subTotalText)
    
    def getCartRow(self, itemName):
        self.rows = self.get_table_rows(CartPageLocators.cartTableRows)
        for row in self.rows:
            if (itemName in row.text):
                return tuple(row.text.split(' $')[1:])
