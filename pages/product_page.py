from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_button.click()

    def get_product_name(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".product_main h1").text

    def get_product_price(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".price_color").text

    def should_be_added_book_name_message(self, book_name):
        #message = self.browser.find_element(*ProductPageLocators.BOOK_NAME_MESSAGE)
        message = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(ProductPageLocators.BOOK_NAME_MESSAGE)
        )
        print(f"✓ Найдено сообщение: {message.text}")
        assert book_name == message.text, f"Название '{book_name}' не найдено в сообщении: {message}"
        print(f"✓ Название '{book_name}' совпадает")

    def should_be_basket_message_with_correct_price(self, book_price):
        #basket_message = self.browser.find_element(*ProductPageLocators.CART_MESSAGE)
        basket_message = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(ProductPageLocators.CART_MESSAGE)
            )
        # В сообщении должна быть общая стоимость корзины, и она должна равняться цене товара
        print(f"✓ Сообщение корзины: {basket_message.text}")
        assert book_price == basket_message.text, f"Цена '{book_price}' не найдена в сообщении корзины: {basket_message.text}"
        print(f"✓ Цена '{book_price}' совпадает")

    def go_to_cart_button(self):
        cart_button = self.browser.find_element(*ProductPageLocators.GO_TO_CART_BUTTON)
        cart_button.click()