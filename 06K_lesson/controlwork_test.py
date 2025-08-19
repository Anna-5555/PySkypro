from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_validation():
    # Инициализация драйвера (в данном случае для Edge)
    driver = webdriver.Edge()

    # Открыть страницу
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    # Заполнить форму
    driver.find_element(By.CSS_SELECTOR,
                        'input[name="first-name"]').send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR,
                        'input[name="last-name"]').send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR,
                        'input[name="address"]').send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR,
                        'input[name="e-mail"]').send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR,
                        'input[name="phone"]').send_keys("+7985899998787")
    # Zip code оставляем пустым
    driver.find_element(By.CSS_SELECTOR,
                        'input[name="city"]').send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR,
                        'input[name="country"]').send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR,
                        'input[name="job-position"]').send_keys("QA")
    driver.find_element(By.CSS_SELECTOR,
                        'input[name="company"]').send_keys("SkyPro")

    # Нажать кнопку Submit
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Проверить, что поле Zip code подсвечено красным
    zip_code = driver.find_element(By.CSS_SELECTOR, 'div[id="zip-code"]')
    assert "alert-danger" in zip_code.get_attribute("class")

    # Проверить, что остальные поля подсвечены зеленым
    valid_fields = [
        'first-name', 'last-name', 'address', 'e-mail',
        'phone', 'city', 'country', 'job-position', 'company'
    ]

    for field in valid_fields:
        element = driver.find_element(By.CSS_SELECTOR, f'div[id="{field}"]')
        assert "alert-success" in element.get_attribute("class")

    driver.quit()
