from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка "Конструктор" в шапке сайта
    BUTTON_CONSTRUCTOR = (By.XPATH, '//p[text() = "Конструктор"]')
    # Кнопка "Лента заказов"
    BUTTON_ORDER_FEED_IN_HEADER = (By.XPATH, "//p[text()='Лента Заказов']")
    # Кнопка "Личный кабинет"
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")

    # Заголовок конструктора
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")

    # Окно "Детали ингредиента"   
    MODAL_OF_INGREDIENT = (By.XPATH, "//section[contains(@class, 'Modal_modal')]")
    # Кнопка с крестиком, закрывающая окно "Детали ингредиента"
    BUTTON_CLOSE_MODAL = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")

    # Оверлей модального окна
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
    # Картинка ингредиента в общем списке
    BURGER_INGREDIENT = (By.XPATH, './/img[@alt="Флюоресцентная булка R2-D3"]')
    # Место,куда перетаскиваются инредиенты
    BASKET_FOR_INGREDIENTS = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket__')]")

    # Количество экземпляров ингредиента в заказе (счетчик)
    COUNT_OF_INGREDIENTS = (By.XPATH, ".//ul[contains(@class, 'BurgerIngredients_ingredients__')]//p[contains(text(),'Флюоресцентная булка R2-D3')]/following-sibling::div//p[contains(@class, 'counter')]")

    # Кнопка "Оформить заказ"
    BUTTON_MAKE_ORDER = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    # Кнопка "Войти в аккаунт"
    BUTTON_LOGIN_TO_ORDER = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")

    # Номер заказа в модальном окне                                                      
    ORDER_MODAL = (By.XPATH, ".//div[contains(@class, 'Modal_modal__container')]")
    # Временный номер заказа(заглушка)
    ORDER_NUMBER_LOADING = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    # финальный номер заказа
    ORDER_NUMBER_CONFIRM = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    # Кнопка с крестиком, закрывающая окно подтвержденного заказа
    BUTTON_CLOSE_CONFIRMATION = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//button[contains(@class, 'Modal_modal__close')]")