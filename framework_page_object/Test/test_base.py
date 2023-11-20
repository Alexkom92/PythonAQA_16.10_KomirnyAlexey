from abc import ABC
import pytest
from selenium.webdriver import Chrome, Firefox


class BaseTest(ABC):
    def __init__(self):
        self.driver = None

    @pytest.fixture
    def setup_method(self, request, browser="chrome"):
        if browser.lower() == "chrome":
            self.driver = Chrome()
        elif browser.lower() == "firefox":
            self.driver = Firefox()
        else:
            raise ValueError(f"Unsupported browser:{browser}")

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        def teardown():
            if self.driver:
                self.driver.quit()

        request.addfinalizer(teardown)
        return self.driver
