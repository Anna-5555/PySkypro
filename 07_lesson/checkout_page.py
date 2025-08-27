from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        return self

    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        return self

    def enter_postal_code(self, postal_code):
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        return self

    def click_continue(self):
        self.driver.find_element(By.ID, "continue").click()
        return self

    def fill_checkout_form(self, first_name, last_name, postal_code):
        return (self.enter_first_name(first_name)
                .enter_last_name(last_name)
                .enter_postal_code(postal_code)
                .click_continue())

    def get_total_amount(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        return total_text.replace("Total: $", "")

