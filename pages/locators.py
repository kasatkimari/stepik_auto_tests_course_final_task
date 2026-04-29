from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    CART_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    GO_TO_CART_BUTTON = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(2) > a:nth-child(1)")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_CART_BUTTON = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")


class CartPageLocators():
    CART_ITEMS = (By.CSS_SELECTOR, '#basket_formset > div')
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')