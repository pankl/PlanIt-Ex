import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Pages.HomePage import HomePage
from Pages.ContactPage import ContactPage
from Pages.ShopPage import ShopPage
from Pages.CartPage import CartPage
from Helpers.Constants import * 
from Helpers.MyLogger import getmylogger
from Helpers.Item import Item



logger = getmylogger(__name__)

class TestPlanItJupiterToys(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.debug('Starting set up for the tests')
        logger.debug('Navigating to home page')
        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        cls.driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
        cls.driver.get(baseUri)
    
    def setUp(self):
        logger.debug('Running setUp method')
        self.homePage = HomePage(TestPlanItJupiterToys.driver)

    def test_verify_validation_errors_on_contact_page(self):
        try:
            self.homePage.clickContactButton()
            logger.debug('Navigating to Contact page')
            self.contactPage = ContactPage(TestPlanItJupiterToys.driver)
            self.contactPage.clickSubmitButton()
            logger.debug('Asserting correct error message is present for Forname field')
            self.assertEqual(fornameErrorMessage,self.contactPage.getErrorMessage('Forename'),
                            f"Expected: {fornameErrorMessage} \r\nInstead got: {self.contactPage.getErrorMessage('Forename')}")
            
            logger.debug('Asserting correct error message is present for Email field')
            self.assertEqual(emailErrorMessage,self.contactPage.getErrorMessage('Email'),
                            f'Expected: {emailErrorMessage} \r\nInstead got: {self.contactPage.getErrorMessage("Email")}')
            
            logger.debug('Asserting correct error message is present for Message field')
            self.assertEqual(messageErrorMessage,self.contactPage.getErrorMessage('Message'),
                            f'Expected: {messageErrorMessage} \r\nInstead got: {self.contactPage.getErrorMessage("Message")}')
        except:
            self.fail() 

    def test_verify_successful_contact_submission(self):
        try:
            self.homePage.clickContactButton()
            logger.debug('Navigating to Contact page')
            self.contactPage = ContactPage(TestPlanItJupiterToys.driver)
            self.contactPage.inputForNameText(forename)
            self.contactPage.inputEmailText(email)
            self.contactPage.inputMessageText(message)
            self.contactPage.clickSubmitButton()
            logger.debug('Asserting success message to show on submission of valid form')
            self.assertEqual(successfulMessage,self.contactPage.getSuccessMessage(),
                            f'Expected: {successfulMessage} \r\nInstead got: {self.contactPage.getSuccessMessage()}')
        except:
            self.fail() 
    
    def test_verify_shopping_cart(self):
        try:
            self.homePage.clickShopButton()
            logger.debug('Navigating to Shop page')
            self.shopPage = ShopPage(TestPlanItJupiterToys.driver)
            
            logger.debug('Adding items to cart')
            '''Adding items to cart and enriching it with expected price and subtotal'''
            self.expectedItemsInCart, self.expectedTotal = self.addItemsToCart(shopItems)
                
            self.homePage.clickCartButton()
            logger.debug('Navigating to Cart page')
            self.cartPage = CartPage(TestPlanItJupiterToys.driver)
            for item in self.expectedItemsInCart:
                logger.debug(f'Asserting expected values for item {item.itemName}')
                itemPriceInCart, itemSubTotalInCart = self.cartPage.getCartRow(item.itemName)
                self.assertEqual(item.itemPrice, float(itemPriceInCart))
                self.assertEqual(item.itemSubTotal, float(itemSubTotalInCart))

            logger.debug('Asserting cart SubTotal')
            actualTotal = float(self.cartPage.getSubTotal().split(":")[1])
            self.assertEqual(self.expectedTotal, actualTotal)
                
        except:
            self.fail()
    

    def tearDown(self):
        logger.debug('Running tearDown method')
        try:
            TestPlanItJupiterToys.driver.get(baseUri)
        except:
            logger.error('Something went wrong when trying to navigate to home page')
            return

    @classmethod    
    def tearDownClass(cls):  
        logger.debug('Running cleanup')
        cls.driver.close() 

    def addItemsToCart(self, items):
        self.tappedItems = list()
        self._expectedSubTotal = 0
        for item in items:
            tapItem = Item(item[0],int(item[1]))
            logger.debug(f'Adding to cart and enriching item {tapItem.itemName}')
            self.shopPage.buyItem(tapItem)
            tapItem.setItemPrice(float(self.shopPage.getItemPrice(tapItem).strip('$')))
            print(tapItem.itemPrice, tapItem.itemName, tapItem.itemQty)
            tapItem.setItemSubTotal(tapItem.itemQty,tapItem.itemPrice)
            self.tappedItems.append(tapItem)
            self._expectedSubTotal += tapItem.itemSubTotal
        return self.tappedItems, self._expectedSubTotal   




if __name__ == '__main__':
    
    suite = unittest.TestSuite()
    suite.addTests(TestPlanItJupiterToys)
    unittest.TextTestRunner(verbosity=2)
    runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Test report', report_name='report',
                            open_in_browser=True, description="HTMLTestReport")
    runner.run(suite)
    unittest.main(testRunner=runner)
