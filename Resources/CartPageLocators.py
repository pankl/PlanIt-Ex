from selenium.webdriver.common.by import By

class CartPageLocators():
    cartTableRows = (By.XPATH, "//table//tbody//tr")
    subTotalText = (By.XPATH, "//*[@class = 'total ng-binding']")