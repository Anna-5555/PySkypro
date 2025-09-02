import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from auth_page_allure import AuthPage
from main_page_allure import MainPage
from cart_page_allure import CartPage
from order_page_allure import OrderPage

import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@allure.title("Тестирование заказа в онлайн магазине")
@allure.description("Тест проверяет процесс заказа в магазине "
                    "и корректность вывода итоговой суммы")
@allure.feature("Онлайн заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    """
    Тест проверяет работау магазина.
    :param driver: WebDriver — объект драйвера, переданный фикстурой
    """

    auth = AuthPage(driver)
    with allure.step("Авторизация пользователя"):
        with allure.step("Ввод логина и пароля"):
            auth.login('standard_user', 'secret_sauce')
        with allure.step("Клик по кнопке 'Login'"):
            auth.login_button()

    main = MainPage(driver)
    with allure.step("Добавление товаров в корзину"):
        with allure.step("Выбор товаров"):
            main.selection_of_product()
        with allure.step("Переход в корзину"):
            main.go_to_cart()

    with allure.step("Подтверждение состава корзины"):
        cart = CartPage(driver)
        cart.checkout()

    order = OrderPage(driver)
    with allure.step("Отправка данных пользователя и "
                     "получение итоговой стоимости заказа"):
        with allure.step("Отправка данных пользователя"):
            order.information_of_buyer('Иван', 'Петров', '123456')
            order.button_continue()
        with allure.step("Получение итоговой суммы заказа"):
            total = order.get_result()

    with allure.step("Проверка итоговой суммы заказа"):
        assert total == '$58.29'
