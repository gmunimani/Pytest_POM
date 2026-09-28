from Page_Layers.login import LoginPage
from Page_Layers.profilemanagement import ProfileManagementPage
from utilities.jsonreader import read_json
from utilities.configreaders import get_config


def test_open_profile(setup):

    driver = setup

    driver.get(get_config("naukri", "url"))

    data = read_json("test_data/profiledata.json")

    login = LoginPage(driver)

    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )

    profile = ProfileManagementPage(driver)

    profile.open_profile()

    assert "profile" in driver.current_url.lower()