import unittest
import sys
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Pages.HomePage import HomePage
from Pages.ContactPage import ContactPage
from Pages.ShopPage import ShopPage
from Helpers.Constants import * 
from Helpers.MyLogger import getmylogger



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

    @unittest.skip("a")
    def test_verify_validation_errors_on_contact_page(self):
        try:
            self.homePage.clickContactButton()
            self.contactPage = ContactPage(TestPlanItJupiterToys.driver)
            self.contactPage.clickSubmitButton()
            logger.debug('Asserting correct error message is present for Forname field')
            
            self.assertEqual(fornameErrorMessage,self.contactPage.getErrorMessage('Forename'),
                            f"Expected: {fornameErrorMessage} \r\nInstead got: {self.contactPage.getErrorMessage('Forename')}")
            
            logger.debug("Asserting correct error message is present for Email field")
            self.assertEqual(emailErrorMessage,self.contactPage.getErrorMessage('Email'),
                            f"Expected: {emailErrorMessage} \r\nInstead got: {self.contactPage.getErrorMessage('Email')}")
            
            logger.debug("Asserting correct error message is present for Message field")
            self.assertEqual(messageErrorMessage,self.contactPage.getErrorMessage('Message'),
                            f"Expected: {messageErrorMessage} \r\nInstead got: {self.contactPage.getErrorMessage('Message')}")
        except:
            self.fail() 

    @unittest.skip("a")
    def test_verify_successful_contact_submission(self):
        try:
            self.homePage.clickContactButton()
            self.contactPage = ContactPage(TestPlanItJupiterToys.driver)
            self.contactPage.inputForNameText(forename)
            self.contactPage.inputEmailText(email)
            self.contactPage.inputMessageText(message)
            self.contactPage.clickSubmitButton()
            logger.debug('Asserting success message to show on submission of valid form')
            self.assertEqual(successfulMessage,self.contactPage.getSuccessMessage(),
                            f"Expected: {successfulMessage} \r\nInstead got: {self.contactPage.getSuccessMessage()}")
        except:
            self.fail() 

    def test_verify_shopping_cart(self):
        try:
            self.homePage.clickShopButton()
            self.shopPage = ShopPage(TestPlanItJupiterToys.driver)
            for item in shopItems:
                self.shopPage.buyItem(item)
                item = item + (self.shopPage.getItemPrice(item), )
                print(item, type(item))
                
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




if __name__ == '__main__':
    
    suite = unittest.TestSuite()
    suite.addTests(TestPlanItJupiterToys)
    unittest.TextTestRunner(verbosity=2)
    runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Test report', report_name='report',
                            open_in_browser=True, description="HTMLTestReport")
    runner.run(suite)
    unittest.main(testRunner=runner)
