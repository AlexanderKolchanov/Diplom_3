from page_objects.account_page import AccountPage
from page_objects.main_page import MainPage
from conftest import *
import allure


class TestAccountPage:

    @allure.title('Проверка перехода в личный кабинет')
    @allure.description('''
    Проверка доступа к личному кабинету после авторизации:
    1. Выполнить вход в систему с валидными учетными данными
    2. Кликнуть на кнопку "Личный кабинет" в хедере сайта
    3. Проверить успешный переход в личный кабинет
    4. Убедиться в отображении кнопки "Выйти" - индикатор авторизации
    ''')
    def test_navigate_to_personal_account_success(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        
        # Авторизуемся в системе с созданными тестовыми данными
        user_credentials = create_new_user_and_delete[0]
        main_page.login(user_credentials['email'], user_credentials['password'])
        
        # Переходим в личный кабинет через кнопку в хедере
        main_page.click_on_personal_account_in_header()
        
        # Проверяем что вход выполнен успешно - кнопка "Выйти" отображается
        assert account_page.check_logout_button_displayed()
        

    @allure.title('Проверка выполнения логаута по кнопке "Выйти"')
    @allure.description('''
    Проверка выхода из учетной записи через личный кабинет:
    1. Выполнить вход в систему
    2. Перейти в личный кабинет
    3. Кликнуть на кнопку "Выйти" для выхода из аккаунта
    4. Проверить успешный выход - появление кнопки "Зарегистрироваться"
    5. Убедиться в перенаправлении на страницу авторизации
    ''')
    def test_logout_from_profile_page_success(self, driver, create_new_user_and_delete):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        
        # Авторизуемся в системе для тестирования выхода
        user_credentials = create_new_user_and_delete[0]
        main_page.login(user_credentials['email'], user_credentials['password'])
        
        # Переходим в личный кабинет где доступна кнопка выхода
        main_page.click_on_personal_account_in_header()
        
        # Выполняем выход из учетной записи
        account_page.click_on_logout_button()
        
        # Проверяем что выход выполнен успешно - появилась кнопка регистрации
        account_page.wait_visibility_of_button_register()
        assert account_page.check_displaying_of_button_register()