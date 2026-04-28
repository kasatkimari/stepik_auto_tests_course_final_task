from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    #Гость открывает главную страницу
    #Переходит в корзину по кнопке в шапке сайта
    #Ожидаем, что в корзине нет товаров
    #Ожидаем, что есть текст о том что корзина пуста
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_cart_button()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_not_have_products()
    cart_page.should_be_empty_cart_message()
    cart_page.get_empty_cart_text()

