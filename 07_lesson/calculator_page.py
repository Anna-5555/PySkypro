from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        return self

    def set_delay(self, seconds):
        delay_field = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys(str(seconds))
        return self

    def enter_expression(self, expression):
        for char in expression:
            if char.isdigit():
                self.click_number(char)
            elif char in "+-*/=":
                self.click_operator(char)
        return self

    def click_number(self, number):
        button = self.driver.find_element(By.XPATH, f"//span[text()='{number}']")
        button.click()
        return self

    def click_operator(self, operator):
        button = self.driver.find_element(By.XPATH, f"//span[text()='{operator}']")
        button.click()
        return self

    def get_result(self, timeout=46):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), ""))
        return self.driver.find_element(By.CLASS_NAME, "screen").text

    def calculate_expression(self, expression, delay=45):
        return (self.open()
                .set_delay(delay)
                .enter_expression(expression)
                .get_result())
