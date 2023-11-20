from framework_page_object.Pages.base_page import BasePage
from framework_page_object.Resources.locators import PersonalAccountLocator


class PersonalAccount(BasePage, PersonalAccountLocator):
    def __init__(self, driver, email, password):
        super().__init__(driver)
        self._driver.get("https://haircp.com.ua/index.php?route=account/login")
        self.__email = email
        self.__password = password

    def account_login(self):
        self.enter_text(self.locator_email, self.__email)
        self.enter_text(self.locator_password, self.__password)
        self.click(self.login_button_locator)
