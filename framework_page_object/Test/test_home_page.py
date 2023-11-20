from framework_page_object.Test.test_base import BaseTest
from framework_page_object.Resources.locators import HomePageLocator

class ersonalAccountTest(BaseTest):
    def __init__(self):
        super().__init__()

    def test_account_login(self, personal_account):
        personal_account.enter_text(self, self.locator_email, self.__email)
        personal_account.enter_text(self, self.locator_password, self.__password)
        personal_account.click(self, self.login_button_locator)
        assert "Добро пожаловать"
