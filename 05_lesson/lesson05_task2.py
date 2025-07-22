from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = (webdriver.Chrome
          (service=ChromeService(ChromeDriverManager().install())))

driver.maximize_window()     # открыть окно по размеру экрана
driver.get("http://uitestingplayground.com/dynamicid")

# Находим кнопку по классу и кликаем
try:
    button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()
    print("✅ Кнопка успешно нажата!")
except Exception as e:
    print(f"❌ Ошибка: {e}")

sleep(20)
