from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = (webdriver.Firefox
          (service=FirefoxService(GeckoDriverManager().install())))

driver.maximize_window()     # открыть окно по размеру экрана
driver.get("http://the-internet.herokuapp.com/login")

# Находим поле ввода
search_input = driver.find_element(By.CSS_SELECTOR, "#username")
# Вводим текст "tomsmith"
search_input.send_keys("tomsmith")
sleep(2)

# Находим поле ввода
search_input = driver.find_element(By.CSS_SELECTOR, "#password")
# Вводим текст "SuperSecretPassword!"
search_input.send_keys("SuperSecretPassword!")
sleep(2)

# Находим кнопку по классу и кликаем
button = driver.find_element(By.CSS_SELECTOR, "i.fa.fa-2x.fa-sign-in")
button.click()
sleep(3)

message = driver.find_element(By.CSS_SELECTOR, '#flash.flash.success')
print_message = message.text
print(print_message)

# Закрываем браузер
driver.quit()
