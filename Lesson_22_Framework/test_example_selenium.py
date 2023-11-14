from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Lesson_22_Framework.test_locators import Locators


class TestByShampoo(Locators):
    def __init__(self):
        super().__init__()

    @staticmethod
    def wait_and_click_test(driver, locator):
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
        element.click()

    def test_01(self):
        driver = Chrome()
        driver.maximize_window()
        try:
            driver.get("https://haircp.com.ua/")
            self.wait_and_click_test(driver, self.main_menu_locator)
            self.wait_and_click_test(driver, self.locator_for_hair)
            self.wait_and_click_test(driver, self.locator_hair_shampoo)
            self.wait_and_click_test(driver, self.locator_shampoo_for_head)
            self.wait_and_click_test(driver, self.locator_filter_shampoo_chi)
            self.wait_and_click_test(driver, self.locator_search_with_filter)
            self.wait_and_click_test(driver, self.locator_chi_shampoo_product)
            self.wait_and_click_test(driver, self.locator_730ml_sku)
            self.wait_and_click_test(driver, self.locator_add_product)
            self.wait_and_click_test(driver, self.locator_buy)

        except Exception as e:
            print(f"Возникло исключение: {e}")
        finally:
            driver.quit()


test_case = TestByShampoo()
test_case.test_01()
