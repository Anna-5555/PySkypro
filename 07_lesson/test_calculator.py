import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


class TestCalculator:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.quit()

    def test_slow_calculator_addition(self):
        # Только создание объекта страницы и assert'ы
        calculator_page = CalculatorPage(self.driver)

        result = (calculator_page.open()
                  .set_delay(45)
                  .enter_expression("7+8=")
                  .get_result())

        assert result == "15"

    def test_calculator_with_fluent_interface(self):
        # Альтернативный вариант с методом calculate_expression
        calculator_page = CalculatorPage(self.driver)

        result = calculator_page.calculate_expression("7+8=", 45)

        assert result == "15"
