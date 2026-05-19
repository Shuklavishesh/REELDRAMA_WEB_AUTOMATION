import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options


def get_driver(browser):

    browser = browser.lower()

    if browser == "chrome":

        options = Options()

        options.add_argument("--start-maximized")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = uc.Chrome(
            options=options,
            use_subprocess=False
        )

        return driver

    raise Exception(
        f"{browser} not supported"
    )