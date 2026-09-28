from Page_Layers.login import LoginPage
from utilities.jsonreader import read_json
from utilities.configreaders import get_config


def test_valid_login(setup):

    driver = setup

    driver.get(get_config("naukri", "url"))

    data = read_json("test_data/profiledata.json")

    login = LoginPage(driver)

    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )

    assert "naukri.com" in driver.current_url