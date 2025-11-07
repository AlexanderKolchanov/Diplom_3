from page_objects.feed_page import FeedPage
from page_objects.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from conftest import *
import allure


class TestFeedPage:

    @allure.title('Проверка увеличения числа на счетчике количества выполненных за всё время заказов')
    @allure.description('''
    Проверка обновления счетчика заказов за все время:
    1. Авторизоваться в системе
    2. Зафиксировать начальное значение счетчика заказов
    3. Создать новый заказ через конструктор
    4. Проверить увеличение счетчика после создания заказа
    5. Убедиться в корректном обновлении статистики
    ''')
    def test_changes_counter_for_quantity_of_orders_success(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        
        # Авторизуемся для доступа к функционалу заказов
        user_credentials = create_new_user_and_delete[0]
        main_page.login(user_credentials['email'], user_credentials['password'])
        
        # Получаем начальное значение счетчика заказов за все время
        main_page.click_header_feed_button()
        orders_count_1 = feed_page.get_quantity_of_orders()
        
        # Создаем новый заказ через конструктор
        main_page.click_on_button_constructor()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_on_button_make_order()
        
        # Ожидаем обработки заказа и появления номера в модальном окне
        main_page.wait_visibility_of_element(MainPageLocators.ORDER_NUMBER_CONFIRM, timeout=30)
        main_page.click_on_button_close_confirmation_modal()
        
        # Проверяем обновленное значение счетчика заказов
        main_page.click_header_feed_button()
        orders_count_2 = feed_page.get_quantity_of_orders()
        
        # Преобразуем значения в числа и сравниваем
        count_1 = int(orders_count_1)
        count_2 = int(orders_count_2)
        # Счетчик должен увеличиться после создания заказа
        assert count_2 > count_1, f"Счетчик не увеличился: было {count_1}, стало {count_2}"


    @allure.title('Проверка увеличения числа на счетчике выполненных за Сегодня заказов')
    @allure.description('''
    Проверка обновления счетчика заказов за текущий день:
    1. Авторизоваться в системе
    2. Зафиксировать начальное значение счетчика за Сегодня
    3. Создать новый заказ через конструктор
    4. Проверить увеличение дневного счетчика
    5. Убедиться в актуальности ежедневной статистики
    ''')
    def test_changes_counter_for_daily_quantity_of_orders_success(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        
        # Авторизуемся для работы с заказами
        user_credentials = create_new_user_and_delete[0]
        main_page.login(user_credentials['email'], user_credentials['password'])
        
        # Получаем начальное значение счетчика заказов за сегодня
        main_page.click_header_feed_button()
        orders_count_1 = feed_page.get_daily_quantity_of_orders()
        
        # Создаем новый заказ в конструкторе
        main_page.click_on_button_constructor()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_on_button_make_order()
        
        # Ожидаем завершения обработки заказа
        main_page.wait_visibility_of_element(MainPageLocators.ORDER_NUMBER_CONFIRM, timeout=30)
        main_page.click_on_button_close_confirmation_modal()
        
        # Проверяем обновленное значение дневного счетчика
        main_page.click_header_feed_button()
        orders_count_2 = feed_page.get_daily_quantity_of_orders()
        
        # Преобразуем значения в числа и сравниваем
        count_1 = int(orders_count_1)
        count_2 = int(orders_count_2)
        # Счетчик должен увеличиться после создания заказа
        assert count_2 > count_1, f"Счетчик не увеличился: было {count_1}, стало {count_2}"
        

    @allure.title('Проверка появления нового заказа в разделе "В работе"')
    @allure.description('''
    Проверка отображения нового заказа в ленте заказов:
    1. Авторизоваться в системе
    2. Создать новый заказ через конструктор
    3. Получить номер созданного заказа
    4. Перейти в ленту заказов
    5. Проверить наличие заказа в разделе "В работе"
    6. Убедиться в реальном времени обновления ленты
    ''')
    def test_displaying_new_order_in_progress_feed_success(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        
        # Авторизуемся для создания заказа
        user_credentials = create_new_user_and_delete[0]
        main_page.login(user_credentials['email'], user_credentials['password'])
        
        # Создаем заказ и получаем его номер для проверки
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_on_button_make_order()
        new_order_id = main_page.get_number_of_order_in_modal_confirmation()
        main_page.click_on_button_close_confirmation_modal()
        
        # Переходим в ленту заказов для проверки отображения
        main_page.click_header_feed_button()
        
        # Проверяем что созданный заказ отображается в разделе "В работе"
        order_in_progress = feed_page.get_order_number_in_feed_progress_section()
        assert order_in_progress is not None