from .base_page import BasePage
from .locators import ProductPageLocators
import math

class ProductPage(BasePage):

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code:{alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_in_basket(self):

        self.should_be_message_product_added_in_basket()
        self.should_be_correct_product_name()
        self.should_be_message_with_basket_price()
        self.should_be_correct_basket_price()


    def should_be_message_product_added_in_basket(self):
        message1=bool(self.browser.find_element(*ProductPageLocators.MASSAGE_ADD_TO_BASKET))
        assert  message1, "Отсутствует сообщение о добавлении товара в корзину"

    def should_be_correct_product_name(self):
        name_book=self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        name_book_in_basket=self.browser.find_element(*ProductPageLocators.NAME_BOOK_IN_BASKET).text
        assert name_book == name_book_in_basket,\
            "Название книги в корзине не совпадает с названием выбранной книги"

    def should_be_message_with_basket_price(self):
        message2=bool(self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_BASKET))
        assert message2, "Отсутствует сообщение о стоимости корзины"

    def should_be_correct_basket_price(self):
        book_price=self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_price=self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert book_price == basket_price, \
            "Цена книги и корзины с одной этой книгой не совпадают"