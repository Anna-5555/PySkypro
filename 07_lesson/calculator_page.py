from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.buttons = {
            "0": (By.XPATH, "//span[text()='0']"),
            "1": (By.XPATH, "//span[text()='1']"),
            "2": (By.XPATH, "//span[text()='2']"),
            "3": (By.XPATH, "//span[text()='3']"),
            "4": (By.XPATH, "//span[text()='4']"),
            "5": (By.XPATH, "//span[text()='5']"),
            "6": (By.XPATH, "//span[text()='6']"),
            "7": (By.XPATH, "//span[text()='7']"),
            "8": (By.XPATH, "//span[text()='8']"),
            "9": (By.XPATH, "//span[text()='9']"),
            "+": (By.XPATH, "//span[text()='+']"),
            "-": (By.XPATH, "//span[text()='-']"),
            "*": (By.XPATH, "//span[text()='×']"),
            "/": (By.XPATH, "//span[text()='÷']"),
            "=": (By.XPATH, "//span[text()='=']"),
            "C": (By.XPATH, "//span[text()='C']")
        }

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        return self

    def set_delay(self, seconds):
        delay_field = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys(str(seconds))
        return self

    def click_button(self, button_name):
        button = self.driver.find_element(*self.buttons[button_name])
        button.click()
        return self

    def enter_expression(self, expression):
        """Вводит выражение посимвольно"""
        for char in expression:
            if char in self.buttons:
                self.click_button(char)
            time.sleep(0.1)  # небольшая пауза между нажатиями
        return self

    def get_result(self, timeout=46):
        # Ждем пока результат не станет числом (не выражением)
        wait = WebDriverWait(self.driver, timeout)

        def is_result_ready(driver):
            current_text = driver.find_element(By.CLASS_NAME, "screen").text
            # Ждем пока текст не станет числом (не выражением типа "7+8")
            return current_text not in ["", "7+8", "7+8="] and current_text.isdigit()

        wait.until(is_result_ready)
        return self.driver.find_element(By.CLASS_NAME, "screen").text

    def calculate_expression(self, expression, delay=45):
        self.open().set_delay(delay)
        self.enter_expression(expression)
        return self.get_result()
