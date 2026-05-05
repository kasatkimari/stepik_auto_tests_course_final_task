from stepik_auto_tests_course_final_task.pages.locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), 'Сообщения о пустой корзине нет, но должно быть'


    def should_not_have_products(self):
        """Проверяем, что в корзине нет товаров"""
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Товары в корзине присутствуют, но не должны"

    def get_empty_basket_text(self):
        """Возвращает текст сообщения о пустой корзине (для дополнительной проверки)"""
        empty_basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        return empty_basket_text