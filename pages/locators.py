from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    Basket_button = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    Book_name = (By.CSS_SELECTOR, "div.product_main h1 ")
    Book_price = (By.CSS_SELECTOR, "div.product_main .price_color")
#****

    Success_messages = (By.CSS_SELECTOR, "div.alertinner strong")


