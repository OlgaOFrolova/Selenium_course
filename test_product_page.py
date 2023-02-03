import pytest
from .pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By

from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

from selenium.common.exceptions import NoAlertPresentException


link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser):

        page = ProductPage(browser, link)

        page.open()
        page.should_be_add_to_basket()
        registration_button = browser.find_element(By.CSS_SELECTOR, "#login_link")
        registration_button.click()

        page = LoginPage(browser, link)
        page.register_new_user()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    try:
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket()
        page.solve_quiz_and_get_code()

    except NoAlertPresentException:
        print("No 2 test alert presented")

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.guest_cant_see_product_in_basket_opened()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

# эти тесты в ревью не входят↓

def test_guest_can_add_product_to_basket(browser):


        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket()
        page.solve_quiz_and_get_code()


def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.Success_messages), \
            "Success message is presented, but should not be"


def should_success_message_disappeared(self):
    assert self.is_disappeared(*ProductPageLocators.Success_messages), \
        "Success message is disappeared"


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    page.should_success_message_disappeared()


#********************************

def test_user_cant_see_success_message(browser):
      try:

         page = ProductPage(browser, link)

         page.open()

         registration_button = browser.find_element(By.CSS_SELECTOR, "#login_link")
         registration_button.click()

         page = LoginPage(browser, link)
         page.register_new_user()


      except NoAlertPresentException:
          print("No alert presented")


          page = ProductPage(browser, link)
          page.should_not_be_success_message()
      finally:
          browser.quit()



