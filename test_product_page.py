from .pages.base_page import BasePage
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time


def test_guest_cant_see_success_message(browser):
    #Открываем страницу товара
    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    #Открываем страницу товара
    #Добавляем товар в корзину
    #Проверяем, что нет сообщения об успехе с помощью is_disappeared
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_button()
    page.should_be_dissapeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()

    book_name = page.get_product_name()
    book_price = page.get_product_price()

    page.add_to_basket_button()
    #page.solve_quiz_and_get_code()
    page.should_be_added_book_name_message(book_name)
    page.should_be_basket_message_with_correct_price(book_price)


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """Гость открывает страницу товара
    Переходит в корзину по кнопке в шапке
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_button()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_have_products()
    basket_page.should_be_empty_basket_message()
    basket_page.get_empty_basket_text()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        # открыть страницу регистрации
        page.open()
        #зарегистрировать нового пользователя;
        email = str(time.time()) + "@fakemail.org"
        password = "Testpassword123!"
        page.register_new_user(email, password)
        #проверить, что пользователь залогинен
        page.should_be_authorized_user()

    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Открываем страницу товара
        # Добавляем товар в корзину
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_button()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()

        book_name = page.get_product_name()
        book_price = page.get_product_price()

        page.add_to_basket_button()
        #page.solve_quiz_and_get_code()
        page.should_be_added_book_name_message(book_name)
        page.should_be_basket_message_with_correct_price(book_price)
