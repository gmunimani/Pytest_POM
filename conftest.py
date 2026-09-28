import pytest

from utilities.browser_setup import get_driver
from utilities.screenshots import take_screenshot


@pytest.fixture
def setup():

    driver = get_driver()

    yield driver

    driver.quit()


def pytest_runtest_makereport(item, call):

    if call.when == "call" and call.excinfo is not None:

        driver = item.funcargs.get("setup")

        if driver:take_screenshot(driver,item.name)