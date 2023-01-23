from pages.base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
       login_url = self.browser.current_url
       assert "/login" in login_url, "login is absent in current url"

       #assert "login" in browser.current_url,  # сообщение об ошибке


    def should_be_login_form(self):


        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM ), "No autorizacion form"


    def should_be_register_form(self):

        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "No register form"

