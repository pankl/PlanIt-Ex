from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


class BasePage():
    """The BasePage class holds all common functionality across the website.
    Also provides a nice wrapper when dealing with selenium functions that may
    not be easy to understand.
    """

    def __init__(self, driver):
        """ This function is called every time a new object of the base class is created"""
        self.driver = driver
        self.ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
        
    
    def click(self, by_locator, timeout=10):
        """ Performs click on web element whose locator is passed to it"""
        WebDriverWait(self.driver, timeout, ignored_exceptions=self.ignored_exceptions).until(EC.presence_of_element_located(by_locator)).click()
    
    def enter_text(self, by_locator, text, timeout=10):
        """ Performs text entry of the passed in text, in a web element whose locator is passed to it"""
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self, by_locator, timeout=10) -> str:
        """Returns the title of the page"""
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator)).get_attribute("innerText")
         
    
    def wait_for_element(self,by_locator,timeout=10):
        """Waits for an element to be on the page"""
        myElem = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(by_locator))
        return myElem
    
    def get_table_rows(self,by_locator,timeout=10):
        """Returns a table row based on value of the first cell"""
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(by_locator))

    def wait_for_element_to_be_clickable(self,by_locator,timeout=10):
         """Waits for a button element to be on the page and clickable"""
         myElem = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(by_locator))

    def wait_for_element_to_be_gone(self,by_locator,timeout=30):
        """Waits for an element to be gone from the page """
        myElem = WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(by_locator))
