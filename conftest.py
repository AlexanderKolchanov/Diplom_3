import pytest
import tempfile
from selenium import webdriver
from urls import Urls
import requests
from helpers import create_random_email, create_random_password, create_random_name


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    """Фикстура для инициализации веб-драйвера с поддержкой Chrome и Firefox
    
    Особенности:
    - Параметризация для тестирования в обоих браузерах
    - Уникальная user-data-dir для Chrome для избежания конфликтов
    - Автоматическое закрытие драйвера после тестов
    """
    browser_name = request.param
    driver = None
    
    try:
        if browser_name == 'firefox':
            options = webdriver.FirefoxOptions()
            options.add_argument('--width=1920')
            options.add_argument('--height=1080')
            driver = webdriver.Firefox(options=options)
        elif browser_name == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
            temp_dir = tempfile.mkdtemp()
            options.add_argument(f"--user-data-dir={temp_dir}")
            driver = webdriver.Chrome(options=options)
        
        driver.implicitly_wait(5)
        driver.get(Urls.BASE_URL)
        yield driver
        
    finally:
        if driver:
            driver.quit()


@pytest.fixture
def create_new_user_and_delete():
    """Фикстура для создания временного пользователя с автоматическим удалением
    
    Создает пользователя с случайными данными для тестов авторизации
    Автоматически удаляет пользователя после завершения теста
    
    Возвращает:
    - tuple: (учетные данные пользователя, данные ответа от API)
    """
    # Генерация случайных учетных данных
    payload_cred = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_name()
    }
    
    # Регистрация пользователя через API
    response = requests.post(Urls.USER_REGISTER, data=payload_cred)
    response_body = response.json()

    # Возврат данных для использования в тестах
    yield payload_cred, response_body

    # Автоматическое удаление пользователя после теста
    access_token = response_body['accessToken']
    requests.delete(Urls.USER_DELETE, headers={'Authorization': access_token})