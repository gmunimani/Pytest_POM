from selenium.webdriver.common.by import By
from utilities.waits import wait_for_element


class ProfileManagementPage:

    def __init__(self, driver):
        self.driver = driver

    profile_image = (By.XPATH,"//div/img[@alt='naukri user profile image']")

    profile_link = (By.XPATH,"//a[text()='View & Update Profile']")

    update_resume = (By.XPATH,"//a[text()='Update']")

    #file_input = (By.CSS_SELECTOR,"input[type='file']")

    def open_profile(self):

        wait_for_element(self.driver,self.profile_image).click()

        wait_for_element(self.driver,self.profile_link).click()

    def upload_resume(self, resume_path):

        # Click Update button if required
        wait_for_element(self.driver,self.update_resume).click()

        # Directly send path to HTML file input
        #wait_for_element(
        #    self.driver,//a[text()='View & Update Profile']
         #   self.file_input
        #).send_keys(resume_path)