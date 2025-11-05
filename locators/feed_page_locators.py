from selenium.webdriver.common.by import By


class FeedPageLocators:
    # Раздел заказов
    SECTION_ORDERS_LIST = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]')

    # Заголовок ленты заказов
    TITLE_OF_ORDERS_FEED = (By.XPATH, '//h1[text()="Лента заказов"]')

    # Всплывающее окно с деталями заказа
    MODAL_ORDER = (By.XPATH, '//section[contains(@class, "Modal_modal")]')

    # Заголовок всплывающего окна с деталями заказа
    TITLE_OF_MODAL_ORDER = (By.XPATH, '//section[contains(@class, "Modal_modal")]//h2')

    # Счетчик заказов "Выполнено за все время"
    ORDER_COUNTER_BY_ALL_TIME = (By.XPATH, "//p[contains(text(),'Выполнено за все время')]/following-sibling::p[contains(@class, 'OrderFeed_number')]")

    # Счетчик заказов "Выполнено за сегодня"
    ORDER_COUNTER_BY_TODAY = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p[contains(@class, 'OrderFeed_number')]")

    # Заказ в разделе "В работе"
    ORDER_IN_PROGRESS = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]//li") 
    
    # Один заказ в истории
    ORDER_FIRST_IN_HISTORY = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem')][1]")
    
    # Все заказы в истории
    ALL_ORDERS_HISTORY = (By.XPATH, './/p[contains(@class, "text_type_digits-default")]')