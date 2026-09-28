from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utilities.waits import wait_for_element

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait=WebDriverWait(driver,10)

    username = (By.ID, "usernameField")

    password = (By.ID, "passwordField")

    login_btn = (By.XPATH,"//button[text()='Login']")

    def login(self, user, pwd):
        wait_for_element(self.driver,self.username).send_keys(user)

        wait_for_element(self.driver,self.password).send_keys(pwd)

        wait_for_element(self.driver,self.login_btn).click()