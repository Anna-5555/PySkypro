from selenium.webdriver.common.by import By
import allure


class AuthPage:
    def __init__(self, driver):
        """
        Конструктор класса AuthPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver

    @allure.step("Ввод логина и пароля ")
    def login(self, username: str, password: str):
        """
        Функция вводит логин и пароль пользователя для авторизации
        """
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(username)
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)

    @allure.step("Клик по кнопке 'Login' для авторизации")
    def login_button(self):
        """
        Функция для нажатия по кнопке 'Login' для авторизации
        """
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()
