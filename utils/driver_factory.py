from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import undetected_chromedriver as uc

def get_driver(browser="chrome"):

    if browser.lower() != "chrome":
        raise Exception(f"Browser '{browser}' not supported")

    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")

    # 🔥 IMPORTANT FIX
    driver = uc.Chrome(version_main=147, options=options)

    return driver