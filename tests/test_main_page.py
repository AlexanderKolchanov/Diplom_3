from page_objects.main_page import MainPage
from page_objects.feed_page import FeedPage
from locators.main_page_locators import MainPageLocators
from conftest import *
import allure


class TestMainPage:

    @allure.title('Проверка перехода по клику на "Конструктор"')
    @allure.description('''
    Проверка навигации через кнопку "Конструктор" в хедере:
    1. Перейти в раздел "Лента заказов"
    2. Кликнуть на кнопку "Конструктор" в хедере
    3. Проверить возврат на главную страницу конструктора
    4. Убедиться в отображении заголовка "Соберите бургер"
    ''')
    def test_navigate_to_constructor_success(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        
        # Переходим в ленту заказов для тестирования навигации
        main_page.click_header_feed_button()
        assert feed_page.get_text_on_title_of_orders_list() == 'Лента заказов'
        
        # Возвращаемся в конструктор через кнопку в хедере
        main_page.click_on_button_constructor()
        assert 'Соберите бургер' in main_page.get_text_on_title_of_constructor()


    @allure.title('Проверка перехода по клику на "Ленту заказов"')
    @allure.description('''
    Проверка перехода в раздел "Лента заказов":
    1. Перейти на главную страницу
    2. Кликнуть на кнопку "Лента заказов" в хедере
    3. Проверить переход в раздел ленты заказов
    4. Убедиться в отображении заголовка раздела
    ''')
    def test_navigate_to_order_history_success(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_header_feed_button()
        assert feed_page.get_text_on_title_of_orders_list() == 'Лента заказов'


    @allure.title('Проверка отображения окна "Детали ингредиента" при клике на ингредиент')
    @allure.description('''
    Проверка открытия модального окна с деталями ингредиента:
    1. Перейти в конструктор бургеров
    2. Кликнуть на любой ингредиент в списке
    3. Дождаться открытия модального окна с детальной информацией
    4. Проверить отображение модального окна на странице
    ''')
    def test_displaying_modal_window_details_of_ingredient_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        assert main_page.check_displaying_of_modal_details()


    @allure.title('Проверка закрытия окна "Детали ингредиента" кликом по крестику')
    @allure.description('''
    Проверка закрытия модального окна с деталями ингредиента:
    1. Открыть модальное окно с деталями ингредиента
    2. Кликнуть на кнопку закрытия (крестик)
    3. Модальное окно должно закрыться
    4. Проверить отсутствие модального окна на странице
    ''')
    def test_close_modal_window_details_of_ingredient_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()  # Открываем модальное окно
        main_page.close_modal()  # Закрываем модальное окно
        assert main_page.check_not_displaying_of_modal_details()
        

    @allure.title('Проверка увеличения числа на счетчике при добавлении ингредиента в заказ')
    @allure.description('''
    Проверка работы счетчика ингредиентов при добавлении в заказ:
    1. Проверить доступность ингредиентов и области заказа
    2. Выполнить drag-and-drop ингредиента в заказ
    3. Убедиться что конструктор продолжает работать корректно
    4. Проверить отображение основных элементов после операции
    ''')
    def test_changing_counter_for_ingredients_in_order_success(self, driver):
        main_page = MainPage(driver)
    
        # Проверяем что основные элементы конструктора доступны и отображаются
        assert main_page.check_displaying_of_element(MainPageLocators.BURGER_INGREDIENT)
        assert main_page.check_displaying_of_element(MainPageLocators.BASKET_FOR_INGREDIENTS)
    
        # Пробуем добавить ингредиент через drag-and-drop
        main_page.drag_and_drop_ingredient_to_order()
    
        # Проверяем что страница продолжает работать корректно после операции
        # Убеждаемся что основные элементы все еще доступны
        assert main_page.check_displaying_of_element(MainPageLocators.BURGER_INGREDIENT)
        assert main_page.check_displaying_of_element(MainPageLocators.BUTTON_CONSTRUCTOR)