       
# import logging
# import time
# import random       
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import TimeoutException
# from utils.json_reader import load_json

# locators = load_json("data/locator.json")["login_page"]
# logger = logging.getLogger(__name__)


# class LoginPage:

#     def __init__(self, driver):
#         self.driver = driver

#     # ✅ Accept cookies
#     def accept_cookies(self):

#         try:
#             cookie_btn = WebDriverWait(self.driver, 5).until(
#                 EC.element_to_be_clickable(
#                     (By.XPATH, "//button[contains(text(),'Accept')]")
#                 )
#             )

#             cookie_btn.click()

#             logger.info("✅ Cookies accepted")

#         except Exception:
#             logger.info("✅ No cookie popup found")

#     # ✅ Wait for complete page load
#     def wait_for_page_ready(self):

#         WebDriverWait(self.driver, 30).until(
#             lambda d: d.execute_script(
#                 "return document.readyState"
#             ) == "complete"
#         )

#     # ✅ Enter mobile number
#     def enter_mobile(self, number):

#         logger.info(f"Entering mobile number: {number}")

#         self.accept_cookies()
#         self.wait_for_page_ready()

#         time.sleep(random.uniform(2, 3))

#         def _mobile_input_ready(d):
#             try:
#                 el = d.find_element(By.XPATH, locators["mobile_input"])
#                 return el if el.is_displayed() else False
#             except Exception:
#                 return False

#         mobile_input = WebDriverWait(self.driver, 30).until(_mobile_input_ready)

#         # click input
#         mobile_input.click()

#         time.sleep(1)

#         # clear old value
#         mobile_input.clear()

#         time.sleep(1)

#         # type mobile number
#         for digit in str(number):

#             mobile_input.send_keys(digit)

#             time.sleep(random.uniform(0.2, 0.4))

#         # trigger React/MUI validation
#         mobile_input.send_keys(Keys.TAB)

#         logger.info("✅ Mobile number entered successfully")

#         time.sleep(2)

#     # ✅ Click Get OTP
#     def click_get_otp(self):

#         try:

#             logger.info("Clicking Get OTP button")

#             # wait until clickable
#             get_otp_btn = WebDriverWait(self.driver, 30).until(
#                 lambda d: (
#                     d.find_element(By.XPATH, locators["get_otp_btn"])
#                     if d.find_element(By.XPATH, locators["get_otp_btn"]).is_displayed()
#                     and d.find_element(By.XPATH, locators["get_otp_btn"]).is_enabled()
#                     else False
#                 )
#             )

#             # scroll into view
#             self.driver.execute_script(
#                 "arguments[0].scrollIntoView({block:'center'});",
#                 get_otp_btn
#             )

#             time.sleep(2)

#             # click button normally
#             get_otp_btn.click()

#             logger.info("✅ Get OTP button clicked")

#             # wait until OTP boxes appear (avoid EC.* that may not exist in this Selenium build)
#             WebDriverWait(self.driver, 30).until(
#                 lambda d: len(d.find_elements(By.XPATH, locators["otp_input"])) > 0
#             )

#             logger.info("✅ OTP screen opened successfully")

#         except TimeoutException:

#             logger.error("❌ OTP screen did not open")

#             raise

#         except Exception as e:

#             logger.error(f"❌ Failed to click Get OTP: {str(e)}")

#             raise

#     # ✅ Enter OTP
#     def enter_otp(self, otp):

#         otp = str(otp).strip()

#         logger.info(f"Entering OTP: {otp}")

#         # wait for OTP boxes
#         WebDriverWait(self.driver, 30).until(
#             lambda d: len(
#                 d.find_elements(
#                     By.XPATH,
#                     locators["otp_input"]
#                 )
#             ) >= len(otp)
#         )

#         # fetch OTP boxes
#         otp_boxes = self.driver.find_elements(
#             By.XPATH,
#             locators["otp_input"]
#         )

#         logger.info(f"OTP boxes found: {len(otp_boxes)}")

#         # validate OTP boxes
#         if len(otp_boxes) < len(otp):

#             raise Exception(
#                 "❌ OTP input boxes not loaded properly"
#             )

#         # enter OTP digit by digit
#         for i in range(len(otp)):

#             # re-fetch every loop (React safe)
#             otp_boxes = self.driver.find_elements(
#                 By.XPATH,
#                 locators["otp_input"]
#             )

#             current_box = otp_boxes[i]

#             # wait until visible and enabled
#             WebDriverWait(self.driver, 20).until(
#                 lambda d: current_box.is_displayed()
#                 and current_box.is_enabled()
#             )

#             # scroll into view
#             self.driver.execute_script(
#                 "arguments[0].scrollIntoView({block:'center'});",
#                 current_box
#             )

#             time.sleep(0.5)

#             # click current box
#             current_box.click()

#             time.sleep(0.5)

#             # clear old value
#             current_box.send_keys(Keys.CONTROL + "a")
#             current_box.send_keys(Keys.DELETE)

#             time.sleep(0.2)

#             # enter single digit
#             current_box.send_keys(otp[i])

#             logger.info(
#                 f"✅ Entered OTP digit {otp[i]} in box {i + 1}"
#             )

#             time.sleep(0.5)

#         logger.info("✅ OTP entered successfully")
        
        

#     # ✅ Verify OTP
#     def verify_otp(self):
#         logger.info("Clicking Verify OTP button")

#         # Wait for button to exist + be interactable (avoid EC.* expected_conditions if not present)
#         verify_btn = WebDriverWait(self.driver, 30).until(
#             lambda d: (
#                 (lambda el: el if (el.is_displayed() and el.is_enabled()) else False)(
#                     d.find_element(By.XPATH, locators["verify_otp_btn"])
#                 )
#                 if True
#                 else False
#             )
#         )

#         # Ensure it's visible (sometimes MUI renders but blocks click briefly)
#         WebDriverWait(self.driver, 30).until(
#             lambda d: verify_btn.is_displayed() and verify_btn.is_enabled()
#         )

#         # Scroll into view
#         self.driver.execute_script(
#             "arguments[0].scrollIntoView({block:'center'});",
#             verify_btn
#         )
#         time.sleep(1)

#         # Remove common overlays/backdrops if present
#         self.driver.execute_script("""
#             let overlays = document.querySelectorAll(
#                 '[class*="overlay"], [class*="backdrop"], [class*="modal"], [role="dialog"]'
#             );
#             overlays.forEach(el => { el.style.display = 'none'; });
#         """)
#         time.sleep(0.5)

#         # Try normal click, then JS fallback
#         try:
#             verify_btn.click()
#         except Exception as e:
#             logger.warning(f"Normal click failed on Verify OTP: {str(e)}; trying JS click")
#             self.driver.execute_script("arguments[0].click();", verify_btn)

#         logger.info("✅ Verify OTP button clicked")
#         # Optionally wait a moment for next screen/state change
#         time.sleep(2)
#     # ✅ Open QR login tab
# def open_qr_login(self):

#     logger.info("Opening QR login")

#     qr_tab = WebDriverWait(self.driver,20).until(
#         EC.element_to_be_clickable(
#             (By.XPATH, locators["qr_tab"])
#         )
#     )

#     qr_tab.click()

#     logger.info("✅ QR tab opened")

#     time.sleep(2)


# # ✅ Verify QR visible
# def verify_qr_visible(self):

#     logger.info("Checking QR visibility")

#     qr_image = WebDriverWait(self.driver,20).until(
#         EC.visibility_of_element_located(
#             (By.XPATH, locators["qr_image"])
#         )
#     )

#     assert qr_image.is_displayed(), \
#         "❌ QR code not visible"

#     logger.info("✅ QR code visible")


# # ✅ Validate QR scan flow
# def verify_qr_scan_flow(self):

#     logger.info("Checking QR scan flow")

#     scan_text = WebDriverWait(self.driver,20).until(
#         EC.visibility_of_element_located(
#             (By.XPATH, locators["qr_scan_text"])
#         )
#     )

#     assert scan_text.is_displayed(), \
#         "❌ Scan instruction not visible"

#     logger.info("✅ QR scan flow visible")


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

        except:

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
            random.uniform(2,3)
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
                random.uniform(
                    .2,.4
                )
            )

        mobile.send_keys(
            Keys.TAB
        )

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

            time.sleep(1)

            try:

                btn.click()

            except:

                self.driver.execute_script(
                    "arguments[0].click();",
                    btn
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
                ) > 0
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
            f"Entering OTP:{otp}"
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

        for i,digit in enumerate(otp):

            boxes = self.driver.find_elements(
                By.XPATH,
                locators["otp_input"]
            )

            box=boxes[i]

            self.driver.execute_script(
                "arguments[0].click();",
                box
            )

            time.sleep(.2)

            box.send_keys(
                Keys.CONTROL+"a"
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
                    locators[
                        "verify_otp_btn"
                    ]
                )
            )
        )

        try:

            verify.click()

        except:

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

        assert txt.is_displayed()

        logger.info(
            "✅ QR flow valid"
        )