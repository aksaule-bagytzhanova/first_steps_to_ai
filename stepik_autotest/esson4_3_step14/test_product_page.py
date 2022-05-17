import pytest
import time
from .pages.locators import Locators
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.locators import BasePageLocators
from .pages.locators import ProductPageLocators


@pytest.mark.user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function",autouse=True)
    def setup(self,browser):
        print("setup")
        password=str(time.time())
        email=password+"@fakemail.org"
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page_login = LoginPage(browser, link)
        page_login.open()
        page_login.register_new_user(email, password)
        page_base = BasePage(browser, link)
        page_base.should_be_authorized_user()

    def test_user_cant_see_success_message(self,browser):
        print("cant see")
        page_product = ProductPage(browser,"http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/")
        page_product.open()
        page_product.click_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        page_product.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        print("product")
        page_product = ProductPage(browser,"http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/")
        page_product.open()
        page_product.click_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        page_product.should_be_in_basket()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page_product = ProductPage(browser,link)
    page_product.open()
    page_base = BasePage(browser, link)
    page_base.click_element(*Locators.VIEW_BASKET)
    page_basket = BasketPage(browser, link)
    page_basket.should_be_empty_basket()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page_product = ProductPage(browser,link)
    page_product.open()
    page_base = BasePage(browser, link)
    page_base.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page_product = ProductPage(browser, link)
    page_product.open()
    page_base = BasePage(browser, link)
    page_base.go_to_login_page()
    page_login=LoginPage(browser, browser.current_url)
    page_login.should_be_login_page()

@pytest.mark.need_review
def test_product_can_to_add_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page_product=ProductPage(browser,link)
    page_product.open()
    page_product.click_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
    page_product.solve_quiz_and_get_code()
    page_product.should_be_in_basket()

@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                               marks=pytest.mark.xfail(reason="some bug")),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser, link):
    page_product=ProductPage(browser,link)
    page_product.open()
    page_product.click_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
    page_product.solve_quiz_and_get_code()
    page_product.should_be_in_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page_product = ProductPage(browser, link)
    page_product.open()
    page_product.click_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
    page_product.should_not_be_success_message()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link="http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page_product = ProductPage(browser, link)
    page_product.open()
    page_product.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page_product = ProductPage(browser, link)
    page_product.open()
    page_product.click_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
    page_product.should_disappear_success_message()