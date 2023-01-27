import time
import pytest
from pages.product_page import ProductPage


# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#
# def test_guest_can_add_product_to_basket(browser):
#
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_add_to_basket()

@pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.parametrize2('link', ["okay_link",
                                      pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6"])

def test_guest_can_add_product_to_basket(browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket()


    # запуск: pytest -s test_product_page.py
