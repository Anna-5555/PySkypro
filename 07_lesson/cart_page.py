from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
        return self

    def get_cart_items_count(self):
        return len(self.driver.find_elements(By.CLASS_NAME, "cart_item"))

    def is_product_in_cart(self, product_name):
        cart_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return any(product_name in item.text for item in cart_items)

