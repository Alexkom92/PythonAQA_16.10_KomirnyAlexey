class Locators:
    def __init__(self):
        self.main_menu_locator = "//a[@custom-popup-link = 'mobile-menu']"
        self.locator_for_hair = "//span[text()='Для волосся'][1]"
        self.locator_hair_shampoo = "//span[text()='Шампуні для волосся']"
        self.locator_shampoo_for_head = "//span[text()='Для шкіри голови'][1]"
        self.locator_filter_shampoo_chi = "//span[. ='CHI']"
        self.locator_search_with_filter = "//button[@data-ocf='button']"
        self.locator_chi_shampoo_product = (
            "//a[@data-prod-title = 'Шампунь відновлюючий з олією аргани (340 мл)']"
        )
        self.locator_730ml_sku = "//div[@data-option-id='236110']"
        self.locator_add_product = "//button[@id='button-plus']"
        self.locator_buy = "//button[@id='button-cart']"
