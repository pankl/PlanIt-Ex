from selenium.webdriver.common.by import By

class ShopPageLocators():
    BuyItemButton = (By.XPATH, "//h4[contains(text(), '{{dynamicContent}}')]/following-sibling::p/a")
    ItemPriceText = (By.XPATH, "//h4[contains(text(), '{{dynamicContent}}')]/following-sibling::p/span")
