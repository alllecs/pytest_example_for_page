from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.reg_page import RegPage
from selenium.webdriver.common.by import By
import time

def test_can_go_to_login_page(browser):
    link = "https://www.mantisbt.org/bugs/my_view_page.php"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    #time.sleep(10)

def test_can_authorization_to_login_page(browser):
    link = "https://www.mantisbt.org/bugs/login_page.php?return=%2Fbugs%2Fmy_view_page.php"
    page = LoginPage(browser, link)
    page.open()
    page.auth_to_login_page("user_name", "password")

def test_should_be_login_page(browser):
    link = "https://www.mantisbt.org/bugs/my_view_page.php"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_can_go_to_reg_page(browser):
    link = "https://www.mantisbt.org/bugs/my_view_page.php"
    page = MainPage(browser, link)
    page.open()
    page.go_to_reg_page()
    #time.sleep(10)

def test_should_be_reg_page(browser):
    link = "https://www.mantisbt.org/bugs/my_view_page.php"
    page = MainPage(browser, link)
    page.open()
    page.should_be_reg_link()

def test_can_registration_to_reg_page(browser):
    link = "https://www.mantisbt.org/bugs/signup_page.php"
    page = RegPage(browser, link)
    page.open()
    page.auth_to_reg_page("user_name", "email@domen.ru")