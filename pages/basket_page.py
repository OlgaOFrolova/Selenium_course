from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BasketPage(BasePage):

   def guest_cant_see_product_in_basket_opened(self):
        self.go_to_basket_page()


        empty_basket_message = self.browser.find_element(By.ID, "content_inner").text
        assert "Your basket is empty. Continue shopping" == empty_basket_message, "Not empty basket "
