import pytest
from framework_page_object.Test.test_base import BaseTest
from framework_page_object.Pages.personal_account import PersonalAccount


class TestPersonalAccount(BaseTest):
    def set_up(self):
        self.pers_account = PersonalAccount(self.driver, "your_email@example.com", "your_password")

    def test_account_login(self):
        self.pers_account.account_login()
        # Добавьте здесь проверки, что вход выполнен успешно
        # Например, можно проверить URL или наличие элемента на странице
        assert "Добро пожаловать" in self.driver.page_source
