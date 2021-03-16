from .base_page import BasePage
from selenium.webdriver.common.by import By

class RegPage(BasePage):
    def auth_to_reg_page(self, user, email):
        login_input = self.find_element(By.XPATH, "//input[@id='username']")
        login_input.send_keys(user)
        pass_input = self.find_element(By.XPATH, "//input[@id='email-field']")
        pass_input.send_keys(email)
        button_input = self.find_element(By.XPATH, "//input[@type='submit']")
        button_input.click()