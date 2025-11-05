from page_objects.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
import allure

class AccountPage(BasePage):
    # === МЕТОДЫ АВТОРИЗАЦИИ ===
    
    @allure.step('Ввести email')
    def enter_email(self, email):
        """Ввод email в поле авторизации"""
        self.send_keys_to_input(AccountPageLocators.INPUT_EMAIL, email)
    
    @allure.step('Ввести пароль')
    def enter_password(self, password):
        """Ввод пароля в поле авторизации"""
        self.send_keys_to_input(AccountPageLocators.INPUT_PASSWORD, password)
    
    @allure.step('Нажать кнопку "Войти"')
    def click_login_button(self):
        """Клик по кнопке входа в систему"""
        self.click_on_element(AccountPageLocators.BUTTON_LOGIN)
    
    @allure.step('Проверить отображение страницы входа')
    def check_login_page_displayed(self):
        """Проверка что страница авторизации загружена"""
        return self.check_displaying_of_element(AccountPageLocators.LOGIN_TITLE)

    @allure.step('Подождать прогрузки кнопки "Зарегистрироваться"')
    def wait_visibility_of_button_register(self):
        """Ожидание появления кнопки регистрации на странице"""
        self.wait_visibility_of_element(AccountPageLocators.BUTTON_REGISTER)

    @allure.step('Проверить отображение кнопки "Зарегистрироваться"')
    def check_displaying_of_button_register(self):
        """Проверка отображения кнопки регистрации (признак страницы входа)"""
        return self.check_displaying_of_element(AccountPageLocators.BUTTON_REGISTER)

    # === МЕТОДЫ ЛИЧНОГО КАБИНЕТА ===
    
    @allure.step('Проверить отображение кнопки "Выйти"')
    def check_logout_button_displayed(self):
        """Проверка наличия кнопки выхода (признак успешной авторизации)"""
        return self.check_displaying_of_element(AccountPageLocators.BUTTON_LOGOUT)

    @allure.step('Кликнуть по кнопке "Выйти"')
    def click_on_logout_button(self):
        """Клик по кнопке выхода из учетной записи"""
        self.click_on_element(AccountPageLocators.BUTTON_LOGOUT)