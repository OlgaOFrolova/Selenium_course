import time

from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.basket_page import BasketPage


#
# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()
#
# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
#
# def test_should_be_login_page(browser):
#
#      link = "http://selenium1py.pythonanywhere.com/accounts/login/"
#      page1 = LoginPage(browser, link)
#      page1.open()
#      # проверки на наличие форм
#      page1.should_be_login_form()
#      page1.should_be_register_form()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
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

