# import pytest
# from pages.header_page import HeaderPage


# def test_header_complete_flow(login):

#     header = HeaderPage(login.driver)
   
#     try:
#         header.verify_logo_visible()
#     except Exception as e:
#         print(f"Logo Failed: {e}")

#     try:
#         header.verify_navigation_pages()
#     except Exception as e:
#         print(f"Navigation Failed: {e}")

#     try:
#         header.verify_subscribe_button()
#     except Exception as e:
#         print(f"Subscribe Failed: {e}")     

#     try:
#         header.verify_menu_header_items()
#     except Exception as e:
#         print(f"Menu Failed: {e}")

#     try:
#         header.verify_dynamic_pages()
#     except Exception as e:
#         print(f"Dynamic Pages Failed: {e}")




# # def test_header_complete_flow(login):

# #     header = HeaderPage(login.driver)

# #     header.verify_logo_visible()

# #     header.verify_navigation_pages()

# #     header.verify_subscribe_button()

# #     header.verify_menu_header_items()

# #     header.verify_dynamic_pages()


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


def test_header_dynamic_pages(login):

    header = HeaderPage(login.driver)

    header.verify_dynamic_pages()



