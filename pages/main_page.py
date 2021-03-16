from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.find_element(By.XPATH, "//div[@class='btn-group btn-corner']/a")
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(By.XPATH, "//div[@class='btn-group btn-corner']/a"), "Login link is not presented"

    def go_to_reg_page(self):
        reg_link = self.find_element(By.XPATH, "//div[@class='btn-group btn-corner']/a")
        reg_link.click()

    def should_be_reg_link(self):
        assert self.is_element_present(By.XPATH, "//div[@class='btn-group btn-corner']/a"), "Login link is not presented"