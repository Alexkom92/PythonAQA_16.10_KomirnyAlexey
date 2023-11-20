from framework_page_object.Pages.base_page import BasePage
from framework_page_object.Resources.locators import HomePageLocator


class HomePage(BasePage, HomePageLocator):
    def __init__(self, driver):
        super().__init__(driver)
        driver.get("https://haircp.com.ua/")
