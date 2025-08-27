import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestShopping:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Firefox()
        yield
        self.driver.quit()

    def test_shopping_cart_total(self):
        # Создание объектов страниц
        login_page = LoginPage(self.driver)
        main_page = MainPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)

        # Шаги теста
        login_page.login_as_standard_user()

        main_page.add_products_to_cart([
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]).go_to_cart()

        cart_page.click_checkout()

        checkout_page.fill_checkout_form("Иван", "Петров", "123456")

        total_amount = checkout_page.get_total_amount()

        # Проверка
        assert total_amount == "58.29"
