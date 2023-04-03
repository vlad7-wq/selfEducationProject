from automationexercise.conftest import SetUp
from automationexercise.src.pages.BasePage import BasePage


class TestSignUp(SetUp):

    def test_title(self):
        base_page = BasePage
        start = SetUp

        start.set_up(self, base_page.base_url)
        assert self.driver.title == base_page.title
