import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.json_reader import load_json

logger = logging.getLogger(__name__)

locators = load_json("data/locator.json")["user_profile_page"]


class UserProfilePage:

    def __init__(self, driver):
        self.driver = driver
        
        
        
    def verify_user_profile_screen(self):
        
        heading = WebDriverWait(self.driver,20).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                locators["user_profile_heading"]
            )
        )
    )

        assert heading.is_displayed(), "User Profile screen not displayed"

        logger.info("✅ User Profile screen displayed")
        
        
    def verify_mobile_number_prefill(self):

        mobile = WebDriverWait(self.driver,20).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                locators["mobile_number_input"]
            )
        )
    )

        value = mobile.get_attribute("value")

        assert value.strip() != "", "Mobile number not prefilled"

        logger.info(f"✅ Mobile : {value}")
        
    def verify_email_prefill(self):

        email = WebDriverWait(self.driver,20).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                locators["email_input"]
            )
        )
    )

        value = email.get_attribute("value")

        assert value.strip() != "", "Email not prefilled"

        logger.info(f"✅ Email : {value}")
        
    def complete_mandatory_profile_details(self):

        full_name = WebDriverWait(self.driver,20).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                locators["full_name_input"]
            )
        )
    )

        if full_name.get_attribute("value") == "":   
            full_name.send_keys("Automation Tester")

        country = self.driver.find_element(
        By.XPATH,
        locators["country_input"]
    )

        if country.get_attribute("value") == "":
            country.send_keys("India")

        country_code = self.driver.find_element(
        By.XPATH,
        locators["country_code_input"]
    )

        if country_code.get_attribute("value") == "":
            country_code.send_keys("+91")

        male = self.driver.find_element(
        By.XPATH,
        locators["gender_male"]
    )

        if not male.is_selected():
            male.click()

        save = self.driver.find_element(
        By.XPATH,
        locators["user_profile_save_btn"]
    )

        save.click()

        logger.info("✅ Mandatory profile details completed")