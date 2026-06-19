import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.json_reader import load_json

logger = logging.getLogger(__name__)

locators = load_json("data/locator.json")["header_page"]


class HeaderPage:

    def __init__(self, driver):
        self.driver = driver

    # ==========================
    # TC_HTB_001
    # Verify Logo Visible
    # ==========================
    def verify_logo_visible(self):

        logo = WebDriverWait(
            self.driver,
            20
        ).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    locators["logo"]
                )
            )
        )

        assert logo.is_displayed(), "❌ Logo is not visible"

        logger.info("✅ Logo is visible")

    # ==========================
    # TC_HTB_002
    # Verify Navigation Pages
    # ==========================
    def verify_navigation_pages(self):

        pages = [
            "home_menu",
            "movies_menu",
            "series_menu",
            "shows_menu"
        ]

        for page in pages:

            menu = WebDriverWait(
                self.driver,
                20
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        locators[page]
                    )
                )
            )

            menu.click()

            time.sleep(2)

            logger.info(
                f"✅ Clicked: {page}"
            )

            logger.info(
                f"Current URL: {self.driver.current_url}"
            )

    # ==========================
    # TC_HTB_003
    # Verify Subscribe Button
    # ==========================
    def verify_subscribe_button(self):

        subscribe = WebDriverWait(
            self.driver,
            20
        ).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    locators["subscribe_btn"]
                )
            )
        )

        assert subscribe.is_displayed(), \
            "❌ Subscribe button is not visible"

        logger.info(
            "✅ Subscribe button is visible"
        )

    # ==========================
    # TC_HTB_004
    # Verify Header Menu Items
    # ==========================
    def verify_menu_header_items(self):
         

        WebDriverWait(self.driver, 20).until(
            lambda d: len(
             d.find_elements(
                 By.XPATH,
                locators["header_nav_items"]
            )
        ) >= 5
    )

        menus = self.driver.find_elements(
         By.XPATH,
         locators["header_nav_items"]
    )

        print(f"Menus found = {len(menus)}")

        menu_names = []

        for menu in menus:
            text = menu.text.strip()

            print(
               f"TEXT='{text}' "
               f"HREF='{menu.get_attribute('href')}'"
        )

            menu_names.append(text)

        expected_menus = [
          "Home",
          "Movies",
          "Series",
          "Shows",
          "Test"
    ]

        for expected in expected_menus:
            
            assert expected in menu_names, \
            f"{expected} menu not found"

        print("✅ All Header Menus Verified Successfully")
        
        
    # ==========================
    # TC_HTB_005
    # Verify Dynamic Pages
    # ==========================
    def verify_dynamic_pages(self):

        pages = [
            "home_menu",
            "movies_menu",
            "series_menu",
            "shows_menu"
        ]

        for page in pages:

            element = WebDriverWait(
                self.driver,
                20
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        locators[page]
                    )
                )
            )

            element.click()

            time.sleep(2)

            logger.info(
                f"✅ Dynamic page clicked: {page}"
            )

            logger.info(
                f"Current URL: {self.driver.current_url}"
            )