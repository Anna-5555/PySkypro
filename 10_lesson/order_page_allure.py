from selenium.webdriver.common.by import By
import allure


class OrderPage:
    def __init__(self, driver):
        """
        Конструктор класса AuthPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver

    @allure.step("Ввод имени, фамилии, индекса пользователя ")
    def information_of_buyer(self, first_name: str, last_name: str, code: str):
        """
        Функция вводит имя, фамилию и почтовый индекс пользователя
        """
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(code)

    @allure.step("Клик по кнопке 'Continue'")
    def button_continue(self):
        """
        Нажимает кнопку 'Continue'
        """
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()

    @allure.step("Получение итоговой суммы заказа")
    def get_result(self) -> str:
        """
        Функция находит итоговую сумму заказа и возвращает сумму заказа
        """
        return  self._driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text.replace('Total: ', '')
    