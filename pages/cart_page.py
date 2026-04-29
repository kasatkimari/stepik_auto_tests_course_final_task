from stepik_auto_tests_course_final_task.pages.locators import CartPageLocators
from .base_page import BasePage

class CartPage(BasePage):
    def should_be_empty_cart_message(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_CART_MESSAGE), 'Сообщения о пустой корзине нет, но должно быть'


    def should_not_have_products(self):
        """Проверяем, что в корзине нет товаров"""
        assert self.is_not_element_present(*CartPageLocators.CART_ITEMS), "Товары в корзине присутствуют, но не должны"

    def get_empty_cart_text(self):
        """Возвращает текст сообщения о пустой корзине (для дополнительной проверки)"""
        empty_cart_text = self.browser.find_element(*CartPageLocators.EMPTY_CART_MESSAGE)
        return empty_cart_text