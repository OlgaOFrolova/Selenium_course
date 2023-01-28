
from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_add_to_basket(self):
        self.should_be_book_name()
        self.should_be_book_price()
        self.should_be_add_button()

        button = self.browser.find_element(*ProductPageLocators.Basket_button)
        button.click()
       # self.should_not_be_success_message() #ожидаем, что там нет сообщения об успешном добавлении в корзину

        self.solve_quiz_and_get_code()
        assert self.is_element_present(*ProductPageLocators.Basket_button), "No clik on basket button "


        self.should_be_success()
        self.check_success_message()



        #self.should_success_message_disappeared()  #элемент присутствует на странице и должен исчезнуть


    def should_be_book_name(self):

        assert self.is_element_present(*ProductPageLocators.Book_name), "Not correct name "
        self.book_name = self.browser.find_element(*ProductPageLocators.Book_name).text


    def should_be_book_price(self):

        assert self.is_element_present(*ProductPageLocators.Book_price), "Not correct price "
        self.book_price = self.browser.find_element(*ProductPageLocators.Book_price).text



    def should_be_success(self):
        assert self.is_element_present(*ProductPageLocators.Success_messages), "Message of Success added product in " \
                                                                               "basket not found "

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.Basket_button), "Button 'Add to basket' is not " \
                                                                                "presented "

    def check_success_message(self):

        self.success_messages = self.browser.find_element(*ProductPageLocators.Success_messages).text
        assert self.book_name == self.success_messages," Bug in book name"

    # методы для элементов, которые появляются или исчезают
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.Success_messages), \
            "Success message is presented, but should not be"
    def should_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.Success_messages), \
            "Success message is disappeared"


