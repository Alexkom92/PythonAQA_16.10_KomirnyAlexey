from selenium.webdriver.common.by import By


class HomePageLocator:
    def __init__(self):
        self.main_menu_locator = (By.XPATH, "//a[@custom-popup-link = 'mobile-menu']")
        self.search_locator = (By.XPATH, "//input[@placeholder='Пошук товару']")
        self.contact_locator = (
            By.XPATH,
            "//ul[@class='hide-mobile']//li//a[.='Контакти']",
        )


class PersonalAccountLocator:
    def __init__(self):
        self.locator_email = "//input[@id='email']"
        self.locator_password = "//input[@id='password']"
        self.login_button_locator = "//button[@name='commit']"
