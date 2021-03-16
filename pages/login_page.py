from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def auth_to_login_page(self, user, passwd):
        login_input = self.find_element(By.XPATH, "//input[@id='username']")
        login_input.send_keys(user)
        button_input = self.find_element(By.XPATH, "//input[@type='submit']")
        button_input.click()
        pass_input = self.find_element(By.XPATH, "//input[@id='password']")
        pass_input.send_keys(passwd)
        button_input = self.find_element(By.XPATH, "//input[@type='submit']")
        button_input.click()
