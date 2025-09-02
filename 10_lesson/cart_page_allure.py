from selenium.webdriver.common.by import By
import allure


class CartPage:
    def __init__(self, driver):
        """
        Конструктор класса AuthPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver

    @allure.step("Клиr по кнопке 'Checkout' ")
    def checkout(self):
        """
        Функция для нажатия на кнопку 'Checkout' и
        подтверждения состава корзины
        """
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()
