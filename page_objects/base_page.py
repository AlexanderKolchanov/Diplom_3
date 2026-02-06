from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
import allure


class BasePage:
    def __init__(self, driver):
        """Инициализация базовой страницы с драйвером браузера"""
        self.driver = driver


    @allure.step('Выполнить JavaScript код')
    def execute_javascript(self, script, *args):
        """Выполнение JavaScript кода на странице"""
        return self.driver.execute_script(script, *args)
    

    @allure.step('Создать ActionChains')
    def create_action_chains(self):
        """Создание цепочки действий для сложных взаимодействий"""
        return ActionChains(self.driver)
        

    @allure.step('Подождать прогрузки элемента')
    def wait_visibility_of_element(self, locator, timeout=20):
        """Ожидание видимости элемента на странице с заданным таймаутом"""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    
    @allure.step('Кликнуть на элемент с обработкой исключений')
    def click_on_element(self, locator):
        """Клик по элементу с обработкой случаев когда элемент перекрыт"""
        try:
            target = self.check_element_is_clickable(locator)
            target.click()
        except ElementClickInterceptedException:
            # Если элемент перекрыт, пробуем кликнуть через JavaScript
            element = self.find_element_with_wait(locator)
            self.execute_javascript("arguments[0].click();", element)


    @allure.step('Найти элемент на странице')
    def find_element_with_wait(self, locator, timeout=20):
        """Поиск элемента с ожиданием его появления на странице"""
        return self.wait_visibility_of_element(locator, timeout)
    
    
    @allure.step('Ввести значение в поле ввода')
    def send_keys_to_input(self, locator, keys):
        """Ввод текста в поле ввода с предварительной очисткой"""
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(keys)


    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source_element, target_element):
        """Универсальный метод для drag-and-drop операций"""
        try:
            # Стандартный метод для Chrome и совместимых браузеров
            ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()
        except:
            # Альтернативный метод для Firefox и других браузеров
            ActionChains(self.driver).click_and_hold(source_element)\
                .move_to_element(target_element)\
                .release()\
                .perform()
        # Ждем обновления интерфейса после перетаскивания
        self.wait_for_ui_update()


    @allure.step('Получить текст на элементе')
    def get_text_on_element(self, locator):
        """Получение текстового содержимого элемента"""
        element = self.find_element_with_wait(locator)
        return element.text
    
    
    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator, timeout=10):
        """Проверка отображения элемента на странице"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except:
            return False
        
        
    @allure.step('Проверить, что элемент не отображается')
    def check_not_displaying_of_element(self, locator, timeout=10):
        """Проверка что элемент не отображается на странице"""
        try:
            self.wait_for_closing_of_element(locator, timeout)
            return True
        except:
            return False
        

    @allure.step('Подождать, пока элемент закроется')
    def wait_for_closing_of_element(self, locator, timeout=20):
        """Ожидание исчезновения элемента со страницы"""
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
    
    
    @allure.step('Проверить кликабельность элемента')
    def check_element_is_clickable(self, locator, timeout=20):
        """Проверка что элемент кликабелен и готов к взаимодействию"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    
    
    @allure.step('Подождать смены текста на элементе')
    def wait_for_element_to_change_text(self, locator, old_text, timeout=30):
        """Ожидание изменения текста элемента с заданного значения"""
        return WebDriverWait(self.driver, timeout).until_not(
            EC.text_to_be_present_in_element(locator, old_text)
        )
    
    
    @allure.step('Ждать обновления UI')
    def wait_for_ui_update(self, timeout=5):
        """Ожидание завершения обновления интерфейса после действий"""
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

        
    @allure.step('Ждать пока элемент получит валидный текст')
    def wait_for_element_to_have_valid_text(self, locator, timeout=30):
        """Ожидание появления валидного текста в элементе"""
        return WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.find_element(*locator).text and 
                          driver.find_element(*locator).text.strip() and 
                          not driver.find_element(*locator).text.isspace())
    
    
    @allure.step('Выполнить JavaScript drag-and-drop')
    def execute_javascript_drag_and_drop(self, source_element, target_element):
        """Выполнение drag-and-drop через JavaScript"""
        self.execute_javascript("""
            var source = arguments[0];
            var target = arguments[1];
            
            var dragStart = new Event('dragstart', { bubbles: true });
            var dragOver = new Event('dragover', { bubbles: true });
            var drop = new Event('drop', { bubbles: true });
            
            source.dispatchEvent(dragStart);
            target.dispatchEvent(dragOver);
            target.dispatchEvent(drop);
        """, source_element, target_element)