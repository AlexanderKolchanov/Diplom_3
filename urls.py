class Urls:
    BASE_URL = 'https://stellarburgers.education-services.ru'
    USER_REGISTER = f'{BASE_URL}/api/auth/register'    # Используется в create_new_user_and_delete
    USER_DELETE = f'{BASE_URL}/api/auth/user'          # Используется в create_new_user_and_delete  
    ORDER_CREATE = f'{BASE_URL}/api/orders'            # Используется (потенциально) для заказов
