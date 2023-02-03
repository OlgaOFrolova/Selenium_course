
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage




def test_should_be_login_page(browser):

         link = "http://selenium1py.pythonanywhere.com/accounts/login/"
         page1 = LoginPage(browser, link)
         page1.open()
     # проверки на наличие форм
         page1.should_be_login_form()
         page1.should_be_register_form()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasketPage(browser, link)
        page.open()
        page.guest_cant_see_product_in_basket_opened()


