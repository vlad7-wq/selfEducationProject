
from selenium import webdriver


def get_base_url():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com/")
