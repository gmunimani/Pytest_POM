from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_element(driver,locator,timeout=10):
    return WebDriverWait(driver,timeout).until(EC.presence_of_element_located(locator))