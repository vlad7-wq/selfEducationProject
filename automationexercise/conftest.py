from selenium import webdriver
from automationexercise.src.pages.BasePage import BasePage


class SetUp:

    driver = webdriver.Chrome()

    def set_up(self, url):
        self.driver.get(url)

    def tear_down(self):
        self.driver.quit()
