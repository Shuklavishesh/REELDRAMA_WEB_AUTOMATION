import pytest
import os
from utils.driver_factory import get_driver
from utils.json_reader import load_json
from logs.logging_config import setup_logger
import undetected_chromedriver as uc


@pytest.fixture
def driver():

    driver = uc.Chrome()
    driver.maximize_window()

    yield driver

    try:
        driver.quit()
    except Exception:
        pass

# Load test data once
TEST_DATA = load_json("data/testdata.json")


# -------------------------------
# 🔧 Pytest CLI Options
# -------------------------------
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--env", action="store", default="qa")


# -------------------------------
# 🌍 Environment Config
# -------------------------------
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


# -------------------------------
# 🚀 Driver Fixture
# -------------------------------
@pytest.fixture(scope="function")
def driver(request, config):

    browser = request.config.getoption("--browser")
    driver = get_driver(browser)

    driver.get(config["base_url"])
    driver.maximize_window()

    yield driver

    driver.quit()


# -------------------------------
# 📊 Logging Setup
# -------------------------------
@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    setup_logger()


# -------------------------------
# 📦 Test Data Fixture
# -------------------------------
@pytest.fixture
def testdata():
    return TEST_DATA


# -------------------------------
# 🔑 Login Fixture (Reusable)
# -------------------------------
@pytest.fixture
def login(driver, testdata):
    from pages.login_page import LoginPage
    from utils.otp_handler import get_otp

    login_page = LoginPage(driver)

    mobile = testdata["valid_user"]["mobile"]

    login_page.enter_mobile(mobile)
    login_page.wait_for_captcha()
    login_page.click_get_otp()

    otp = get_otp(mobile)
    login_page.enter_otp(otp)

    return login_page