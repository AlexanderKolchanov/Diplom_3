from page_objects.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.account_page_locators import AccountPageLocators
from selenium.webdriver.common.action_chains import ActionChains
import allure

class MainPage(BasePage):
    
    @allure.step('Кликнуть по кнопке перехода в личный кабинет в хэдере')
    def click_on_personal_account_in_header(self):
        """Клик по кнопке личного кабинета в верхней панели навигации"""
        self.click_on_element(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)


    @allure.step('Кликнуть по кнопке "Лента заказов" в хэдере')
    def click_header_feed_button(self):
        """Клик по кнопке перехода в ленту заказов в хедере"""
        self.click_on_element(MainPageLocators.BUTTON_ORDER_FEED_IN_HEADER)


    @allure.step('Переход на страницу конструктора')
    def click_on_button_constructor(self):
        """Клик по кнопке конструктора для возврата на главную страницу"""
        self.click_on_element(MainPageLocators.BUTTON_CONSTRUCTOR)


    @allure.step('Получение главного заголовка конструктора')
    def get_text_on_title_of_constructor(self):
        """Получение текста заголовка конструктора для проверки навигации"""
        return self.get_text_on_element(MainPageLocators.CONSTRUCTOR_TITLE)
    

    @allure.step('Кликнуть по кнопке "Войти в аккаунт" на главной')
    def click_on_button_login_in_main(self):
        """Клик по кнопке входа в аккаунт на главной странице"""
        self.click_on_element(MainPageLocators.BUTTON_LOGIN_TO_ORDER)


    @allure.step('Кликнуть по ингредиенту')
    def click_on_ingredient(self):
        """Клик по ингредиенту для открытия модального окна с деталями"""
        self.click_on_element(MainPageLocators.BURGER_INGREDIENT)


    @allure.step('Проверить отображение окна "Детали ингредиента"')
    def check_displaying_of_modal_details(self):
        """Проверка отображения модального окна с деталями ингредиента"""
        return self.check_displaying_of_element(MainPageLocators.MODAL_OF_INGREDIENT)
    

    @allure.step('Проверить, что окно "Детали ингредиента" не отображается')
    def check_not_displaying_of_modal_details(self):
        """Проверка что модальное окно с деталями ингредиента закрыто"""
        try:
            self.wait_for_closing_of_element(MainPageLocators.MODAL_OF_INGREDIENT, timeout=10)
            return True
        except:
            return False
        

    @allure.step('Закрыть окно "Детали ингредиента"')
    def close_modal(self):
        """Закрытие модального окна кликом по крестику"""
        self.click_on_element(MainPageLocators.BUTTON_CLOSE_MODAL)


    @allure.step('Добавить ингредиенты')
    def drag_and_drop_ingredient_to_order(self):
        """Добавление ингредиента в заказ через drag-and-drop"""
        try:
            source_element = self.find_element_with_wait(MainPageLocators.BURGER_INGREDIENT)
            target_element = self.find_element_with_wait(MainPageLocators.BASKET_FOR_INGREDIENTS)
            
            # Пробуем JavaScript drag-and-drop
            try:
                self.driver.execute_script("""
                    var source = arguments[0];
                    var target = arguments[1];
                    
                    var dragStart = new Event('dragstart', { bubbles: true });
                    var dragOver = new Event('dragover', { bubbles: true });
                    var drop = new Event('drop', { bubbles: true });
                    
                    source.dispatchEvent(dragStart);
                    target.dispatchEvent(dragOver);
                    target.dispatchEvent(drop);
                """, source_element, target_element)
            except:
                # Метод 2: Через ActionChains
                try:
                    ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()
                except:
                    # Метод 3: Пошаговый ActionChains
                    ActionChains(self.driver).click_and_hold(source_element)\
                        .move_to_element(target_element)\
                        .pause(0.5)\
                        .release()\
                        .perform()
            
            # Даем время для обновления интерфейса
            self.wait_for_ui_update()
            
        except Exception:
            # Просто пробрасываем исключение без дополнительной информации
            raise


    @allure.step('Получить количество ингредиентов')
    def get_count_of_ingredients(self):
        """Получение значения счетчика добавленных ингредиентов"""
        try:
            self.wait_visibility_of_element(MainPageLocators.COUNT_OF_INGREDIENTS, timeout=10)
            count_text = self.get_text_on_element(MainPageLocators.COUNT_OF_INGREDIENTS)
            return count_text if count_text else "0"
        except:
            return "0"
        

    @allure.step('Кликнуть на кнопку создания заказа')
    def click_on_button_make_order(self):
        """Клик по кнопке оформления заказа"""
        self.click_on_element(MainPageLocators.BUTTON_MAKE_ORDER)


    @allure.step('Проверить отображение окна о создании заказа')
    def check_displaying_of_confirmation_modal_of_order(self):
        """Проверка отображения модального окна подтверждения заказа"""
        return self.check_displaying_of_element(MainPageLocators.ORDER_MODAL)
    

    @allure.step('Получить номер в окне о создании заказа')
    def get_number_of_order_in_modal_confirmation(self):
        """Получение номера созданного заказа из модального окна"""
        order_element = self.find_element_with_wait(MainPageLocators.ORDER_NUMBER_CONFIRM, timeout=30)
        self.wait_for_element_to_have_valid_text(MainPageLocators.ORDER_NUMBER_CONFIRM, timeout=30)
        return self.get_text_on_element(MainPageLocators.ORDER_NUMBER_CONFIRM)
    

    @allure.step('Кликнуть на кнопку закрытия окна о создании заказа')
    def click_on_button_close_confirmation_modal(self):
        """Закрытие модального окна с номером заказа"""
        self.click_on_element(MainPageLocators.BUTTON_CLOSE_CONFIRMATION)
        

    @allure.step('Выполнить вход в аккаунт')
    def login(self, email, password):
        """Полный процесс авторизации пользователя"""
        self.click_on_element(MainPageLocators.BUTTON_LOGIN_TO_ORDER)
        self.send_keys_to_input(AccountPageLocators.INPUT_EMAIL, email)
        self.send_keys_to_input(AccountPageLocators.INPUT_PASSWORD, password)
        self.click_on_element(AccountPageLocators.BUTTON_LOGIN)
        self.wait_visibility_of_element(MainPageLocators.BUTTON_MAKE_ORDER, timeout=15)