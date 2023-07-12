from selenium.webdriver.common.by import By

class ContactPageLocators():
    SubmitButton = (By.XPATH, "//*[@class='btn-contact btn btn-primary']")
    ForeNameInput = (By.ID, "forename")
    EmailInput = (By.ID, "email")
    MessageInput = (By.ID, "message")

    ErrorMessage = (By.ID, "{{dynamicContent}}-err")

    SubmitProgressBar = (By.XPATH, "//*[@class='progress progress-info wait']")

    SuccessfulSubmissionMessage = (By.XPATH, "//*[@class='alert alert-success']")
