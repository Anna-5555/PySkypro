from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    driver = webdriver.Chrome()

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Установка задержки
    delay_field = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_field.clear()
    delay_field.send_keys("45")

    # Вычисления
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Ожидание результата
    wait = WebDriverWait(driver, 46)
    wait.until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "screen"), "15"))

    # Проверка
    result = driver.find_element(By.CLASS_NAME, "screen").text
    assert result == "15"

    driver.quit()

