from selenium.webdriver.common.by import By

class Locators():
    VIEW_BASKET=(By.CSS_SELECTOR,"span .btn.btn-default")

class BasePageLocators():
    LOGIN_LINK=(By.CSS_SELECTOR,"#login_link")
    LOGIN_LINK_INVALID=(By.CSS_SELECTOR,"#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, "i.icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM=(By.CSS_SELECTOR,"#register_form")
    LOGIN_FORM=(By.CSS_SELECTOR,"#login_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET=(By.CSS_SELECTOR,".btn.btn-lg.btn-primary.btn-add-to-basket")
    MASSAGE_ADD_TO_BASKET=(By.CSS_SELECTOR,"#messages>.alert:nth-child(1)>div")
    NAME_BOOK_IN_BASKET=(By.CSS_SELECTOR,"#messages>.alert:nth-child(1)>.alertinner >strong")
    NAME_BOOK=(By.CSS_SELECTOR,".col-sm-6.product_main h1")
    MESSAGE_PRICE_BASKET=(By.CSS_SELECTOR,"#messages>.alert:nth-child(3)>div>p")
    BASKET_PRICE=(By.CSS_SELECTOR,"#messages>.alert:nth-child(3) >div >p >strong")
    BOOK_PRICE=(By.CSS_SELECTOR,".col-sm-6.product_main p")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasketPageLocators():
    BASKET_ITEMS=(By.CSS_SELECTOR,"basket-items")
    MESSAGE_VIEW_BASKET = (By.CSS_SELECTOR, "#content_inner p")
