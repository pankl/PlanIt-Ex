from selenium.webdriver.common.by import By

class ContactPageLocators():
    SubmitButton = (By.XPATH, "//*[@class='btn-contact btn btn-primary']")
    ForeNameInput = (By.ID, "forename")
    EmailInput = (By.ID, "email")
    MessageInput = (By.ID, "message")

    ForeNameErrorMessage = (By.ID, "forename-err")
    EmailErrorMessage = (By.ID, "email-err")
    MessageErrorMessage = (By.ID, "message-err")

    SubmitProgressBar = (By.XPATH, "//*[@class='progress progress-info wait']")

    SuccessfulSubmissionMessage = (By.XPATH, "//*[@class='alert alert-success']")
