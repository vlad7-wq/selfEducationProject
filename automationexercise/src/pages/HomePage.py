from selenium.webdriver.common.by import By
from automationexercise.conftest import SetUp


class HomePageLocators:
    SIGNUP_LOGIN = (By.XPATH, "//*[@href='/login']")


class HomePage:

    def __int__(self, driver):
        self.driver = driver
