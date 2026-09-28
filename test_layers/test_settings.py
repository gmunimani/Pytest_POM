from Page_Layers.login import LoginPage
from Page_Layers.settings import SettingsPage
from utilities.jsonreader import read_json
from utilities.configreaders import get_config


def test_communication_settings(setup):

    driver = setup

    driver.get(get_config("naukri", "url"))

    data = read_json("test_data/profiledata.json")

    login = LoginPage(driver)

    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )

    settings = SettingsPage(driver)

    settings.open_communication_settings()

    assert "communication" in driver.current_url.lower()