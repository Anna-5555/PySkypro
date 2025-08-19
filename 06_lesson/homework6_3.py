from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

# Перейти на страницу
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Дождаться загрузки всех картинок
# Ждем, пока все изображения загрузятся (проверяем по последнему изображению)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((
        By.CSS_SELECTOR, "#image-container img:nth-child(4)"))
)

# Получить значение атрибута src у 3-й картинки
third_image = driver.find_element(
    By.CSS_SELECTOR, "#image-container img:nth-child(3)")
src_attribute = third_image.get_attribute("src")

# Вывести значение в консоль
print(src_attribute)

# Закрытие браузера
driver.quit()
