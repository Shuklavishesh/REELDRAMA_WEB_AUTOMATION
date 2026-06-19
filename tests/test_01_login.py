import pytest
from pages.login_page import LoginPage
from selenium.common.exceptions import TimeoutException

pytestmark = pytest.mark.order(1)



# ==============================
# Common Login Helper
# ==============================
def login_with_otp(driver, testdata, otp):

    login = LoginPage(driver)

    login.enter_mobile(
        testdata["valid_user"]["mobile"]
    )

    login.click_get_otp()

    login.enter_otp(otp)

    return login


# ==============================
# MOBILE VALIDATION
# ==============================

def test_valid_login(driver, testdata):

    login = login_with_otp(
        driver,
        testdata,
        testdata["otp"]["valid"]
    )

    login.verify_otp()



def test_login_mobile_invalid_short(
        driver,
        testdata
):

    login = LoginPage(driver)

    login.enter_mobile(
        testdata["invalid_user"]["mobile_short"]
    )

    with pytest.raises(
        TimeoutException
    ):
        login.click_get_otp()



def test_login_mobile_invalid_alpha(
        driver,
        testdata
):

    login = LoginPage(driver)

    login.enter_mobile(
        testdata["invalid_user"]["mobile_alpha"]
    )

    with pytest.raises(
        TimeoutException
    ):
        login.click_get_otp()



def test_login_mobile_blank(driver):

    pytest.xfail(
        "Blank mobile validation pending"
    )


# ==============================
# OTP VALIDATION
# ==============================

def test_login_wrong_otp(
        driver,
        testdata
):

    login = login_with_otp(
        driver,
        testdata,
        testdata["otp"]["invalid"]
    )

    login.verify_otp()



def test_blank_otp(
        driver,
        testdata
):

    login = LoginPage(driver)

    login.enter_mobile(
        testdata["valid_user"]["mobile"]
    )

    login.click_get_otp()

    # login.verify_button_disabled()



def test_incomplete_otp(
        driver,
        testdata
):

    login = LoginPage(driver)

    login.enter_mobile(
        testdata["valid_user"]["mobile"]
    )

    login.click_get_otp()

    login.enter_otp("123")

    # login.verify_button_disabled()



def test_login_expired_otp():

    pytest.xfail(
        "Expired OTP simulation pending"
    )


# ==============================
# QR VALIDATION
# ==============================

def test_login_qr_visibility(driver):

    login = LoginPage(driver)

    login.verify_qr_visible()



def test_login_qr_scan_flow(driver):

    login = LoginPage(driver)

    login.verify_qr_visible()

    login.verify_qr_scan_flow()


# ==============================
# EMAIL VALIDATION
# ==============================

def test_login_email_mode():

    pytest.xfail(
        "Email login pending"
    )  
    
    
# =================================
# TC_ReSend_OTP_Validation_015
# Verify resend sends new OTP
# =================================

# TC_ReSend_OTP_Validation_015
# Verify resend sends new OTP

def test_resend_otp_sends_new_otp(
        driver,
        testdata
):

    login = LoginPage(driver)

    login.enter_mobile(
        testdata["valid_user"]["mobile"]
    )

    login.click_get_otp()

    login.enter_otp("123456")

    driver.save_screenshot("before_resend.png")

    login.click_resend_otp()

    driver.save_screenshot("after_resend.png")

    login.verify_otp_boxes_empty()

# =================================
# TC_ReSend_OTP_Validation_016
# Verify OTP boxes reset
# =================================

def test_resend_otp_boxes_reset(
        driver,
        testdata
):

    login = LoginPage(driver)


    login.enter_mobile(
        testdata["valid_user"]["mobile"]
    )


    login.click_get_otp()


    login.enter_otp(
        "123456"
    )


    login.click_resend_otp()


    login.verify_otp_boxes_empty()



# =================================
# TC_ReSend_OTP_Validation_017
# Verify max resend limit
# =================================

def test_resend_otp_limit(
        driver,
        testdata
):

    login = LoginPage(driver)


    login.enter_mobile(
        testdata["valid_user"]["mobile"]
    )


    login.click_get_otp()


    login.verify_resend_limit()



# =================================
# TC_ReSend_OTP_Validation_018
# Login using new OTP after resend
# =================================

def test_login_after_resend_otp(
        driver,
        testdata
):

    login = LoginPage(driver)


    login.enter_mobile(
        testdata["valid_user"]["mobile"]
    )


    login.click_get_otp()


    login.click_resend_otp()


    login.enter_otp(
        testdata["otp"]["valid"]
    )


    login.verify_otp()