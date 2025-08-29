from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_name):
        add_button_id = f"add-to-cart-{product_name.lower().replace(' ', '-')}"
        self.driver.find_element(By.ID, add_button_id).click()
        return self

    def add_products_to_cart(self, product_names):
        for product_name in product_names:
            self.add_product_to_cart(product_name)
        return self

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        return self
