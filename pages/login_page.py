from selenium.webdriver.common.by import By
import time
from .base_page import BasePage
from .locators import LoginPageLocators



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

   # метод регистрирующий пользователя

    def register_new_user(self):

        email = str(time.time()) + "@fakemail.org"

        input_email = self.browser.find_element(By.ID, "id_registration-email")
        input_email.send_keys(email)
        input_pass = self.browser.find_element(By.ID, "id_registration-password1")
        input_pass.send_keys('4mcB9hVHtfWWDzY')
        input_pass2 = self.browser.find_element(By.ID, "id_registration-password2")
        input_pass2.send_keys('4mcB9hVHtfWWDzY')
        login_button = self.browser.find_element(By.CSS_SELECTOR, "#register_form > button")
        login_button.click()



