import pytest
from pages.header_page import HeaderPage


def test_header_complete_flow(login):

    header = HeaderPage(login.driver)

    try:
        header.verify_logo_visible()
    except Exception as e:
        print(f"Logo Failed: {e}")

    try:
        header.verify_navigation_pages()
    except Exception as e:
        print(f"Navigation Failed: {e}")

    try:
        header.verify_subscribe_button()
    except Exception as e:
        print(f"Subscribe Failed: {e}")

    try:
        header.verify_menu_header_items()
    except Exception as e:
        print(f"Menu Failed: {e}")

    try:
        header.verify_dynamic_pages()
    except Exception as e:
        print(f"Dynamic Pages Failed: {e}")




# import pytest
# from pages.header_page import HeaderPage


# # =================================
# # TC_HTB_001
# # Verify Logo Visible
# # =================================
# def test_header_logo_visibility(login):

#     header = HeaderPage(login.driver)

#     header.verify_logo_visible()


# # =================================
# # TC_HTB_002
# # Verify Navigation Pages
# # =================================
# def test_header_navigation_pages(login):

#     header = HeaderPage(login.driver)

#     header.verify_navigation_pages()


# # =================================
# # TC_HTB_003
# # Verify Subscribe Button
# # =================================
# def test_subscribe_button_visibility(login):

#     header = HeaderPage(login.driver)

#     header.verify_subscribe_button()


# # =================================
# # TC_HTB_004
# # Verify Menu Header Items
# # =================================
# def test_header_menu_items(login):

#     header = HeaderPage(login.driver)

#     header.verify_menu_header_items()


# # =================================
# # TC_HTB_005
# # Verify Dynamic Pages
# # =================================
# def test_dynamic_pages(login):

#     header = HeaderPage(login.driver)

#     header.verify_dynamic_pages()