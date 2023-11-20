from abc import ABC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(ABC):
    def __init__(self, driver):
        self._driver = driver
        self.web_driver_wait = WebDriverWait(self._driver, 10)

    def click(self, locator):
        """Performs click on web element whose locator is passed to it"""
        element = self.web_driver_wait.until(
            EC.visibility_of_element_located((By.XPATH, locator))
        )
        element.click()

    def enter_text(self, locator, text):
        return self.web_driver_wait.until(
            EC.visibility_of_element_located((By.XPATH, locator))
        ).send_keys(text)

