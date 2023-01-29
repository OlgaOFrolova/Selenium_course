# import pytest
# from pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By

from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.base_page import BasePage
import time

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


# def test_guest_can_add_product_to_basket(browser):
#
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_add_to_basket()

# def test_guest_should_see_login_link_on_product_page(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
# def test_guest_can_go_to_login_page_from_product_page(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()

# @pytest.mark.parametrize('link',
#                              ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# @pytest.mark.parametrize2('link', ["okay_link",
#                                       pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6"])

# def test_guest_can_add_product_to_basket(browser, link):
#         page = ProductPage(browser, link)
#         page.open()
#         page.should_be_add_to_basket()


    # запуск: pytest -s test_product_page.py
# def should_not_be_success_message(self):
#         assert self.is_not_element_present(*ProductPageLocators.Success_messages), \
#             "Success message is presented, but should not be"
#

# def should_success_message_disappeared(self):
#     assert self.is_disappeared(*ProductPageLocators.Success_messages), \
#         "Success message is disappeared"
#
#
# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_add_to_basket()
#     page.should_not_be_success_message()


# def test_guest_cant_see_success_message(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()


# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_add_to_basket()
#     page.should_success_message_disappeared()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.guest_cant_see_product_in_basket_opened()

    # button = browser.find_element(By.CSS_SELECTOR, " div.basket-mini.pull-right.hidden-xs > span > a")
    # button.click()
    # time.sleep(2)
    #
    # empty_basket_message = browser.find_element(By.ID, "content_inner").text
    # assert "Your basket is empty. Continue shopping" == empty_basket_message, "Not empty basket "
    # time.sleep(2)
