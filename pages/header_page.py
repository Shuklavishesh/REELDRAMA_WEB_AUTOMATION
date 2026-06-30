import email
from email.mime import message
import logging
import profile
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
          "Clip",
          "Test2"
    ]

        for expected in expected_menus:
            
            assert expected in menu_names, \
            f"{expected} menu not found"

        print("✅ All Header Menus Verified Successfully")
        
    
    
    def verify_profile_menu_navigation(self):
        

        menu_items = [
         ("my_account", "My Account"),
         ("subscription_devices", "Subscription & Devices"),
         ("my_watchlist", "My watchlist"),
         ("continue_watching", "Continue watching"),
         ("child_lock", "Child lock"),
         ("help_support", "Help & Support")
    ]

        for locator_name, menu_name in menu_items: 
        # Open Profile Menu
            profile = WebDriverWait(
            self.driver,
            20
        ).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    locators["profile_icon"]
                )
            )
        )

            profile.click()

        # Click Menu Item
            menu = WebDriverWait(
              self.driver,
             20
        ).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    locators[locator_name]
                )
            )
        )

            logger.info(f"Clicking: {menu_name}")

            menu.click()

            time.sleep(2)

            logger.info(
             f"✅ {menu_name} opened successfully"
        )

            print(
             f"{menu_name} URL = {self.driver.current_url}"
        )

            self.driver.back()

            time.sleep(2)
            
            
    def open_subscription_devices(self):
        profile = WebDriverWait(
        self.driver,
        20
    ).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                locators["profile_icon"]
            )
        )
    )

        profile.click()
        WebDriverWait(
        self.driver,
        20
    ).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                locators["subscription_devices"]
            )
        )
    ).click()

        logger.info("✅ Subscription & Devices opened")
            
            
    def verify_my_account_page(self):

    # Open Profile Menu
        profile = WebDriverWait(
        self.driver,
        20
        ).until(
            EC.element_to_be_clickable(
            (
                By.XPATH,
                locators["profile_icon"]
            )
        )
    )

        profile.click()

    # Click My Account
        my_account = WebDriverWait(
          self.driver,
          20
        ).until(
            EC.element_to_be_clickable(
            (
                By.XPATH,
                locators["my_account"]
            )
        )
    )

        my_account.click()

    # Verify Heading
        heading = WebDriverWait(
          self.driver,
           20
    ).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                locators["my_account_heading"]
            )
        )
    )

        assert heading.is_displayed(), \
           "My Account heading not displayed"

    # Verify User Name
        username = WebDriverWait(
        self.driver,
          20
    ).until(
         EC.visibility_of_element_located(
        (
            By.XPATH,
            locators["profile_name"]
        )
    )
)

        assert username.text.strip() != "", \
            "User name is empty"

    # Verify Mobile Number
        mobile = WebDriverWait(
        self.driver,
        20
    ).until(
      EC.visibility_of_element_located(
        (
            By.XPATH,
            locators["profile_mobile"]
        )
    )
)
        assert mobile.text.strip() != "", \
        "Mobile number is empty"

        email = self.driver.find_element(
           By.XPATH,
          locators["email_value"]
    )

        gender = self.driver.find_element(
        By.XPATH,
        locators["gender_value"]
    )

        dob = self.driver.find_element(
        By.XPATH,
        locators["dob_value"]
    )

        country = self.driver.find_element(
        By.XPATH,
        locators["country_value"]
    )

        country_code = self.driver.find_element(
        By.XPATH,
        locators["country_code_value"]
    )

        remove_account = self.driver.find_element(
        By.XPATH,
        locators["remove_account_label"]
    )

        assert email.text.strip() != ""
        assert gender.text.strip() != ""
        assert dob.text.strip() != ""
        assert country.text.strip() != ""
        assert country_code.text.strip() != ""
        assert remove_account.is_displayed()
       

        logger.info("✅ My Account Page Verified")
        
        logger.info(f"Username      : {username.text}")
        logger.info(f"Mobile        : {mobile.text}")
        logger.info(f"Email        : {email.text}")
        logger.info(f"Gender       : {gender.text}")
        logger.info(f"DOB          : {dob.text}")
        logger.info(f"Country      : {country.text}")
        logger.info(f"Country Code : {country_code.text}")
        logger.info(f"remove_account : {remove_account.text}")
        
    def verify_edit_profile_page(self):

    # Click Edit Profile

        edit_profile = WebDriverWait(
        self.driver,
        20
    ).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                locators["edit_profile_btn"]
            )
        )
    )

        edit_profile.click()

        logger.info("✅ Edit Profile clicked")

    # Verify Edit Profile Page

        heading = WebDriverWait(
          self.driver,
          20
    ).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                locators["edit_profile_heading"]
            )
        )
    )

        assert heading.is_displayed(), \
         "Edit My Profile page not opened"

        logger.info("✅ Edit My Profile page opened")

    # Verify Full Name field

        full_name = WebDriverWait(
           self.driver,
           20
    ).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                locators["full_name_input"]
            )
        )
    )
        time.sleep(1)
        assert full_name.is_displayed(), \
        "Full Name field not visible"

        full_name_value = full_name.get_attribute("value")

        assert full_name_value.strip() != "", \
        "Full Name is empty"
        
        time.sleep(2)
        
        logger.info(
          f"✅ Full Name Found : {full_name_value}"
    )
        
        
        mobile = self.driver.find_element(
        By.XPATH,
        locators["mobile_number_input"]
    )

        mobile_value = mobile.get_attribute("value")

        assert mobile_value.strip() != "", \
        "Mobile Number is empty"
        
     

        logger.info(
          f"✅ Mobile Number : {mobile_value}"
    )

    # Email

        email = self.driver.find_element(
         By.XPATH,
         locators["email_input"]
    )

        email_value = email.get_attribute("value")

        assert email_value.strip() != "", \
        "Email is empty"

        logger.info(
        f"✅ Email : {email_value}"
    )

    # Country

        country = self.driver.find_element(
        By.XPATH,
        locators["country_input"]
    )

        country_value = country.get_attribute("value")

        assert country_value.strip() != "", \
        "Country is empty"

        logger.info(
         f"✅ Country : {country_value}"
    )

    # Country Code

        country_code = self.driver.find_element(
          By.XPATH,
          locators["country_code_input"]
    )

        country_code_value = country_code.get_attribute("value")

        assert country_code_value.strip() != "", \
        "Country Code is empty"

        logger.info(
        f"✅ Country Code : {country_code_value}"
    )

    # Date Of Birth

        dob = self.driver.find_element(
         By.XPATH,
         locators["dob_input"]
    )

        dob_value = dob.get_attribute("value")

        assert dob_value.strip() != "", \
        "DOB is empty"

        logger.info(
        f"✅ DOB : {dob_value}"
    )
        time.sleep(2)
        
        logger.info(
        "✅ All Edit Profile Details Verified Successfully"
    )
       
    def verify_gender(self):
        gender = WebDriverWait(
        self.driver,
        20
    ).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                locators["gender_value"]
            )
        )
    )

        gender_value = gender.text.strip()

        assert gender_value != "", "Gender is empty"

        assert gender_value.lower() in [
            "male",
            "female",
            "other"
    ],  f"Invalid gender: {gender_value}"

        logger.info(f"✅ Gender : {gender_value}")
        
    #VERIFY_SUBSCRIPTION
        
    def verify_subscription_devices_page(self):

        heading = WebDriverWait(
        self.driver,
        20
    ).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                locators["subscription_heading"]
            )
        )
    )

        assert heading.is_displayed()

        logger.info(f"✅ {heading.text}")


        no_plan = WebDriverWait(
        self.driver,
        20
    ).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                locators["no_active_plan"]
            )
        )
    )

        assert no_plan.is_displayed()

        logger.info(f"✅ {no_plan.text}")


        message = WebDriverWait(
        self.driver,
        20
    ).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                locators["no_active_plan_message"]
            )
        )
    )

        assert message.is_displayed()
        logger.info(f"✅ {message.text}")
        
        
    def verify_view_subscription_button(self):

        btn = WebDriverWait(
        self.driver,
        20
    ).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                locators["view_subscription_btn"]
            )
        )
    )

        assert btn.is_displayed()

        logger.info("✅ View Subscription Plans button displayed")

        btn.click()

        WebDriverWait(
        self.driver,
        20
    ).until(
        EC.url_contains("/subscription")
    )

        assert "/subscription" in self.driver.current_url

        logger.info(f"✅ Redirected : {self.driver.current_url}")

    # Back to Subscription & Devices page
        self.driver.back()

        WebDriverWait(
        self.driver,
        20
    ).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                locators["this_device_heading"]
            )
        )
    )

        logger.info("✅ Returned to Subscription & Devices page")
            
   #UPGRADE     
       
    # def verify_upgrade_button(self):

    #     upgrade = WebDriverWait(self.driver,20).until(
    #     EC.element_to_be_clickable(
    #         (By.XPATH, locators["upgrade_btn"])
    #     )
    # )

    #     assert upgrade.is_displayed()
    #     assert upgrade.is_enabled()

    #     logger.info("✅ Upgrade button displayed")

    #     upgrade.click()

    #     logger.info("✅ Upgrade button clicked")
       
    #    #TRANSACTION
        
    def verify_transaction_history(self):

        transaction = WebDriverWait(self.driver,20).until(
        EC.element_to_be_clickable(
            (By.XPATH, locators["transaction_history_btn"])
        )
    )

        assert transaction.is_displayed()
        assert transaction.is_enabled()

        logger.info("✅ Transaction History button displayed")

        transaction.click()

        logger.info("✅ Transaction History button clicked")
        logger.info(f"Current URL = {self.driver.current_url}")
        
    def verify_this_device(self):

        WebDriverWait(self.driver,20).until(
        lambda d: "tab=subscription-devices" in d.current_url
    )

        heading = WebDriverWait(
        self.driver,
        20
    ).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                locators["this_device_heading"]
            )
        )
    )

        self.driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        heading
    )

        device = WebDriverWait(
        self.driver,
        20
    ).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                locators["device_name"]
            )
        )
    )

        last_used = WebDriverWait(
        self.driver,
        20
    ).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                locators["last_used"]
            )
        )
    )

        assert heading.is_displayed()
        assert device.is_displayed()
        assert last_used.is_displayed()

        logger.info(f"✅ {heading.text}")
        logger.info(f"✅ Device : {device.text}")
        logger.info(f"✅ {last_used.text}")