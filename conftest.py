
import logging
import pytest
from utils.driver_factory import get_driver
from utils.json_reader import load_json
from logs.logging_config import setup_logger
from pages.login_page import LoginPage


TEST_DATA = load_json("data/testdata.json")


def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chrome"
    )

    parser.addoption(
        "--env",
        action="store",
        default="qa"
    )


# Enable console logging
def pytest_configure(config):

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )


@pytest.fixture(scope="session")
def config(request):

    env = request.config.getoption("--env")

    env_data = {
        "qa": {
            "base_url": "https://qa.reeldrama.com"
        },
        "prod": {
            "base_url": "https://www.reeldrama.com"
        }
    }

    return env_data[env]


@pytest.fixture(scope="function")
def driver(request, config):

    browser = request.config.getoption("--browser")

    driver = get_driver(browser)

    driver.get(config["base_url"])

    driver.maximize_window()

    yield driver

    try:
        if driver and driver.session_id:
            driver.quit()

    except Exception:
        pass


@pytest.fixture(scope="session", autouse=True)
def setup_logging():

    setup_logger()


@pytest.fixture
def testdata():

    return TEST_DATA


# @pytest.fixture
# def login(driver, testdata):

#     from pages.login_page import LoginPage
#     from utils.otp_handler import get_otp_from_api

#     login_page = LoginPage(driver)

#     mobile = testdata["valid_user"]["mobile"]

#     login_page.enter_mobile(mobile)

#     login_page.click_get_otp()

#     otp = get_otp_from_api(mobile)

#     login_page.enter_otp(otp)

#     login_page.verify_otp()

#     return login_page


@pytest.fixture
def login(driver, testdata):


    login_page = LoginPage(driver)

    mobile = testdata["valid_user"]["mobile"]

    login_page.enter_mobile(mobile)

    login_page.click_get_otp()

    otp = testdata["otp"]["valid"]

    print(f"OTP Used = {otp}")

    login_page.enter_otp(otp)

    login_page.verify_otp()

    return login_page



