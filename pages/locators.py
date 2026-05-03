from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    # Форма логина
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_USERNAME = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login_form > button')

    # Форма регистрации
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR,'#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR,'#register_form > button')


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    CART_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    GO_TO_CART_BUTTON = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_CART_BUTTON = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGOUT_LINK = (By.CSS_SELECTOR, "a[href*='logout']")  # ссылка "Выйти"
    ACCOUNT_LINK = (By.CSS_SELECTOR, "a[href*='accounts']")  # ссылка на аккаунт


class CartPageLocators():
    CART_ITEMS = (By.CSS_SELECTOR, '#basket_formset > div')
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')