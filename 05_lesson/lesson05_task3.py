from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = (webdriver.Firefox
          (service=FirefoxService(GeckoDriverManager().install())))

driver.maximize_window()     # открыть окно по размеру экрана
driver.get("http://the-internet.herokuapp.com/inputs")

search_locator = "input"

# Находим поле ввода
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
# Вводим текст "Sky"
search_input.send_keys("Sky", Keys.RETURN)
sleep(2)
# Очищаем поле
search_input.clear()
sleep(2)

# Вводим текст "Pro"
search_input.send_keys("Pro", Keys.RETURN)
sleep(2)

# Закрываем браузер
driver.quit()