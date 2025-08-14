from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

# Перейти на страницу
driver.get("http://uitestingplayground.com/textinput")

# Ввести текст SkyPro в поле ввода
input_field = driver.find_element(By.ID, "newButtonName")
input_field.clear()
input_field.send_keys("SkyPro")

# Нажать на синюю кнопку
button = driver.find_element(By.ID, "updatingButton")
button.click()

# Получить текст кнопки после изменения
# Ждем пока текст кнопки изменится (максимум 10 секунд)
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
)

# Получаем окончательный текст кнопки
button_text = button.text

# Вывести текст в консоль
print(button_text)  # Должно вывести: "SkyPro"

# Закрытие браузера
driver.quit()
