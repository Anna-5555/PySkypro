from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        return self

    def enter_username(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        return self

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)
        return self

    def click_login(self):
        self.driver.find_element(By.ID, "login-button").click()
        return self

    def login_as_standard_user(self):
        return (self.open()
                .enter_username("standard_user")
                .enter_password("secret_sauce")
                .click_login())

