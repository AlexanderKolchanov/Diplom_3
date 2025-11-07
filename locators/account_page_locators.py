from selenium.webdriver.common.by import By

class AccountPageLocators:
    """Локаторы для страницы авторизации и аккаунта"""
    
    # Форма авторизации
    AUTH_FORM = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']")
    
    # Поля ввода
    INPUT_EMAIL = (By.XPATH, ".//input[@name = 'name']")
    INPUT_PASSWORD = (By.XPATH, ".//input[@name = 'Пароль']")
    
    # Кнопки авторизации
    BUTTON_LOGIN = (By.XPATH, "//button[text() = 'Войти']")
    BUTTON_REGISTER = (By.XPATH, "//a[text() = 'Зарегистрироваться']")
    BUTTON_RECOVER = (By.XPATH, "//a[text() = 'Восстановить пароль']")
    
    # Заголовок страницы входа
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")
    
    # Локаторы для личного кабинета
    BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(), 'Выход')]")