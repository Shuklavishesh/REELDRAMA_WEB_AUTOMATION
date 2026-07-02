import pytest

from pages.header_page import HeaderPage

pytestmark = pytest.mark.order(2)


def test_header_logo(login):

    header = HeaderPage(login.driver)

    header.verify_logo_visible()


def test_header_navigation(login):

    header = HeaderPage(login.driver)

    header.verify_navigation_pages()


def test_header_subscribe(login):

    header = HeaderPage(login.driver)

    header.verify_subscribe_button()


def test_header_menu(login):

    header = HeaderPage(login.driver)

    header.verify_menu_header_items()


# def test_header_dynamic_pages(login):

#     header = HeaderPage(login.driver)

#     header.verify_dynamic_pages()
    
def test_profile_menu_navigation(login):

    header = HeaderPage(login.driver)

    header.verify_profile_menu_navigation()
    
    
def test_my_account_page(login):

    header = HeaderPage(login.driver)

    header.verify_my_account_page()
    
    
def test_edit_profile_page(login):

    header = HeaderPage(login.driver)

    header.verify_my_account_page()
    header.verify_gender()

    header.verify_edit_profile_page()
    
# def test_subscription_devices(login):

#     header = HeaderPage(login.driver)

#     header.open_subscription_devices()

#     header.verify_subscription_devices_page()

#     header.verify_view_subscription_button()

#     header.verify_transaction_history()

#     header.verify_this_device()

def test_subscription_devices(login):

    header = HeaderPage(login.driver)

    header.open_subscription_devices()

    header.verify_subscription_devices_page()

    header.verify_view_subscription_button()

    header.verify_transaction_history()

    header.verify_logo_navigation_and_this_device()