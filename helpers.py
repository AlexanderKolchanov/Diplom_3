from faker import Faker

# Инициализация генераторов случайных данных
fake = Faker()        # Генератор для международных данных
fakeRU = Faker(locale='ru_RU')  # Генератор для русскоязычных данных


def create_random_email():
    """Генерация случайного email адреса для тестовых пользователей"""
    email = fake.free_email()
    return email


def create_random_password():
    """Генерация сложного случайного пароля для тестовых аккаунтов
    
    Возвращает пароль длиной 10 символов, содержащий:
    - Специальные символы
    - Цифры
    - Заглавные буквы
    - Строчные буквы
    """
    password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return password


def create_random_name():
    """Генерация случайного русского имени для тестовых пользователей"""
    username = fakeRU.first_name()
    return username