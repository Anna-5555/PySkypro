from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

# Перейти на страницу
driver.get("http://uitestingplayground.com/ajax")

# Нажать на синюю кнопку
ajax_button = driver.find_element(By.ID, "ajaxButton")
ajax_button.click()

# Дождаться появления зеленой плашки и получить текст
success_message = WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
)
message_text = success_message.text

# Вывести текст в консоль
print(message_text)
# Сообщение на печать: "Data loaded with AJAX get request."

# Закрытие браузера
driver.quit()
