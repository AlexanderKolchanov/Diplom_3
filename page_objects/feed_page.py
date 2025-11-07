from page_objects.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
import allure

class FeedPage(BasePage):
    
    @allure.step('Получить текст заголовка раздела заказов')
    def get_text_on_title_of_orders_list(self):
        """Получение заголовка страницы ленты заказов для проверки навигации"""
        return self.get_text_on_element(FeedPageLocators.TITLE_OF_ORDERS_FEED)

    @allure.step('Получить количество заказов, выполненных за все время')
    def get_quantity_of_orders(self):
        """Получение значения счетчика заказов за все время"""
        self.find_element_with_wait(FeedPageLocators.ORDER_COUNTER_BY_ALL_TIME)
        return self.get_text_on_element(FeedPageLocators.ORDER_COUNTER_BY_ALL_TIME)

    @allure.step('Получить количество заказов, выполненных за сегодня')
    def get_daily_quantity_of_orders(self):
        """Получение значения счетчика заказов за текущий день"""
        self.find_element_with_wait(FeedPageLocators.ORDER_COUNTER_BY_TODAY)
        return self.get_text_on_element(FeedPageLocators.ORDER_COUNTER_BY_TODAY)

    @allure.step('Получить номер последнего заказа в разделе "В работе"')
    def get_order_number_in_feed_progress_section(self):
        """Получение номера заказа из раздела 'В работе' в ленте заказов"""
        return self.get_text_on_element(FeedPageLocators.ORDER_IN_PROGRESS)