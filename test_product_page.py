
from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    #browser.get(link)
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()




    # запуск: pytest -s test_product_page.py
