from selenium.webdriver.common.by import By
import allure


class MainPage:
    def __init__(self, driver):
        """
        Конструктор класса AuthPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver

    @allure.step("Выбор товаров в корзину ")
    def selection_of_product(self):
        """
        Функция находит и кладет товары в корзину
        """
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    @allure.step("Переход в корзину")
    def go_to_cart(self):
        """
        Функция для перехода в корзину
        """
        self._driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()
