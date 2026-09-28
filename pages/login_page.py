import logging
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from utils.json_reader import load_json

locators = load_json("data/locator.json")["login_page"]
logger = logging.getLogger(__name__)


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # =============================
    # Accept cookies
    # =============================
    def accept_cookies(self):

        try:
            cookie_btn = WebDriverWait(
                self.driver, 5
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[contains(text(),'Accept')]"
                    )
                )
            )

            cookie_btn.click()

            logger.info(
                "✅ Cookies accepted"
            )

        except Exception:
            logger.info(
                "No cookie popup"
            )

    # =============================
    # Wait page ready
    # =============================
    def wait_for_page_ready(self):

        WebDriverWait(
            self.driver,
            30
        ).until(
            lambda d:
            d.execute_script(
                "return document.readyState"
            ) == "complete"
        )

    # =============================
    # Enter mobile
    # =============================
    def enter_mobile(self, number):

        logger.info(
            f"Entering mobile: {number}"
        )

        self.accept_cookies()
        self.wait_for_page_ready()

        time.sleep(
            random.uniform(2, 3)
        )

        mobile = WebDriverWait(
            self.driver,
            30
        ).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    locators["mobile_input"]
                )
            )
        )

        mobile.click()
        mobile.clear()

        for digit in str(number):

            mobile.send_keys(
                digit
            )

            time.sleep(
                random.uniform(.2, .4)
            )

        mobile.send_keys(Keys.TAB)

        logger.info(
            "✅ Mobile entered"
        )

    # =============================
    # Click Get OTP
    # =============================
    def click_get_otp(self):

        try:

            btn = WebDriverWait(
                self.driver,
                30
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        locators["get_otp_btn"]
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                btn
            )

            # time.sleep(1)

            try:
                btn.click()

            except Exception:

                self.driver.execute_script(
                    "arguments[0].click();",
                    btn
                )

            # WebDriverWait(
            #     self.driver,
            #     30
            # ).until(
            #     lambda d:
            #     len(
            #         d.find_elements(
            #             By.XPATH,
            #             locators["otp_input"]
            #         )
            #     ) > 0
            # )
            
            WebDriverWait(
                self.driver,
                30
            ).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        locators["otp_input"]
                    )
                )
            )

            logger.info(
                "✅ OTP screen opened"
            )

        except TimeoutException:

            logger.error(
                "❌ OTP not opened"
            )

            raise

    # =============================
    # Enter OTP
    # =============================
    def enter_otp(self, otp):

        otp = str(otp).strip()

        logger.info(
            f"Entering OTP: {otp}"
        )

        WebDriverWait(
            self.driver,
            30
        ).until(
            lambda d:
            len(
                d.find_elements(
                    By.XPATH,
                    locators["otp_input"]
                )
            ) >= len(otp)
        )

        for i, digit in enumerate(otp):

            boxes = self.driver.find_elements(
                By.XPATH,
                locators["otp_input"]
            )

            box = boxes[i]

            self.driver.execute_script(
                "arguments[0].click();",
                box
            )

            time.sleep(.2)

            box.send_keys(
                Keys.CONTROL + "a"
            )

            box.send_keys(
                Keys.DELETE
            )

            box.send_keys(
                digit
            )

            logger.info(
                f"Digit {digit} entered"
            )

            time.sleep(.3)

        logger.info(
            "✅ OTP entered"
        )

    # =============================
    # Verify OTP
    # =============================
    def verify_otp(self):

        verify = WebDriverWait(
            self.driver,
            30
        ).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    locators["verify_otp_btn"]
                )
            )
        )

        try:
            verify.click()

        except Exception:

            self.driver.execute_script(
                "arguments[0].click();",
                verify
            )

        logger.info(
            "✅ Verify clicked"
        )

    # =============================
    # Verify QR visible
    # =============================
    def verify_qr_visible(self):

        qr = WebDriverWait(
            self.driver,
            30
        ).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    locators["qr_image"]
                )
            )
        )

        assert qr.is_displayed()

        logger.info(
            "✅ QR visible"
        )
        
        
        
    # =============================
    # Verify QR Scan flow
    # =============================
    def verify_qr_scan_flow(self):

        try:

            self.wait_for_page_ready()
            
            time.sleep(3)

            txt = WebDriverWait(
                self.driver,
                30
            ).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        locators["qr_scan_text"]
                    )
                )
            )
            
            self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            txt
        )

            assert txt.is_displayed(), \
                "QR scan text not visible"

            logger.info(
            f"✅ QR text found: {txt.text}"
        )

        except Exception as e:

            self.driver.save_screenshot(
                "qr_failure.png"
            )

            logger.error(
                f"❌ QR failed: {str(e)}"
            )

            raise
        
        
   
    # =============================
    # Click Resend OTP
    # =============================
    def click_resend_otp(self):

        logger.info("Waiting for Resend OTP button")
        resend_btn = WebDriverWait(
            self.driver,
            150
        ).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    locators["resend_otp_btn"]
                )
            )
        )

        resend_btn.click()

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    locators["otp_sent_confirmation"]
                )
            )
        )

        logger.info("✅ Resend OTP confirmed")

    def verify_otp_boxes_match(self, expected_otp):
        expected_values = list(str(expected_otp).strip())

        def find_expected_boxes(driver):
            boxes = driver.find_elements(
                By.XPATH,
                locators["otp_input"]
            )
            return boxes if len(boxes) == len(expected_values) else False

        boxes = WebDriverWait(
            self.driver,
            10
        ).until(find_expected_boxes)
        values = [box.get_attribute("value") for box in boxes]

        assert values == expected_values, (
            f"Expected OTP boxes to retain {expected_values}, got {values}"
        )

        logger.info("✅ OTP boxes retain the entered digits after resend")
    
    # =============================
    # Resend OTP limit check
    # =============================
    def verify_resend_limit(self):
        
        count = 0


        for i in range(5):
            

            try:

                self.click_resend_otp()
                count += 1

                logger.info(
                f"Resend count: {count}"
            )

                time.sleep(3)


            except Exception:
                logger.info(
                "Resend stopped by application"
            )

            break
        
        assert count > 0, \
        "❌ Resend OTP not working"


        logger.info(
        "✅ Resend OTP limit validation completed"
    )