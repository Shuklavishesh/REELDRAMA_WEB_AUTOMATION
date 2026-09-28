import re
import subprocess
import sys

import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options


def _get_chrome_major_version(browser_executable):
    if sys.platform == "win32":
        import winreg

        registry_keys = (
            (winreg.HKEY_CURRENT_USER, r"Software\Google\Chrome\BLBeacon"),
            (winreg.HKEY_LOCAL_MACHINE, r"Software\Google\Chrome\BLBeacon"),
            (
                winreg.HKEY_LOCAL_MACHINE,
                r"Software\WOW6432Node\Google\Chrome\BLBeacon",
            ),
        )
        for hive, key in registry_keys:
            try:
                with winreg.OpenKey(hive, key) as chrome_key:
                    version, _ = winreg.QueryValueEx(chrome_key, "version")
                version_match = re.match(r"(\d+)\.", version)
                if version_match:
                    return int(version_match.group(1))
            except FileNotFoundError:
                continue

    version_output = subprocess.run(
        [browser_executable, "--version"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    version_match = re.search(r"\b(\d+)\.", version_output)
    if not version_match:
        raise RuntimeError(
            f"Could not determine Chrome's major version from: {version_output!r}"
        )
    return int(version_match.group(1))


def get_driver(browser):

    browser = browser.lower()

    if browser == "chrome":

        options = Options()

        options.add_argument("--start-maximized")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        browser_executable = uc.find_chrome_executable()
        if not browser_executable:
            raise RuntimeError("Could not find a Chrome executable")

        driver = uc.Chrome(
            browser_executable_path=browser_executable,
            version_main=_get_chrome_major_version(browser_executable),
            options=options,
            use_subprocess=True
        )

        return driver

    raise Exception(f"{browser} not supported")

