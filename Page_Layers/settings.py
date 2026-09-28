from selenium.webdriver.common.by import By
from utilities.waits import wait_for_element


class SettingsPage:

    def __init__(self, driver):
        self.driver = driver

    profile_image = (
        By.XPATH,"//div/img[@alt='naukri user profile image']")

    communication_settings = (By.XPATH,"//a[@href='https://www.naukri.com/mnjuser/settings/communication']")

    def open_communication_settings(self):

        wait_for_element(self.driver,self.profile_image).click()

        wait_for_element(self.driver,self.communication_settings).click()