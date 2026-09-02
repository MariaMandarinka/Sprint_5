from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators, StellarBurgersUrls
from helpers import login_user

class TestStellarBurgersLogin:

    # --- БЛОК 1: ВХОД В АККАУНТ (4 ТЕСТА) ---

    # 1. Вход по кнопке «Войти в аккаунт» на главной странице
    def test_login_from_main_page(self, driver):
        driver.get(StellarBurgersUrls.BASE_URL)
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.MAIN_LOGIN_BUTTON)).click()
        login_user(driver, "maria_test_login@yandex.ru", "password123")
        # Ассерт с ожиданием кнопки «Оформить заказ» в качестве маркера успеха
        assert WebDriverWait(driver, 8).until(EC.presence_of_element_located(StellarBurgersLocators.MAIN_ORDER_BUTTON)).is_displayed()

    # 2. Вход через кнопку «Личный кабинет» в шапке сайта
    def test_login_via_personal_account_button(self, driver):
        driver.get(StellarBurgersUrls.BASE_URL)
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.HEADER_PROFILE_BUTTON)).click()
        login_user(driver, "maria_test_login@yandex.ru", "password123")
        assert WebDriverWait(driver, 8).until(EC.presence_of_element_located(StellarBurgersLocators.MAIN_ORDER_BUTTON)).is_displayed()

    # 3. Вход через ссылку на форме регистрации
    def test_login_from_registration_form(self, driver):
        driver.get(StellarBurgersUrls.BASE_URL)
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.MAIN_LOGIN_BUTTON)).click()
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.REG_LOGIN_LINK)).click()
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.REG_LOGIN_LINK)).click()
        login_user(driver, "maria_test_login@yandex.ru", "password123")
        assert WebDriverWait(driver, 8).until(EC.presence_of_element_located(StellarBurgersLocators.MAIN_ORDER_BUTTON)).is_displayed()

    # 4. Вход через ссылку на форме восстановления пароля
    def test_login_from_forgot_password_page(self, driver):
        driver.get(StellarBurgersUrls.BASE_URL)
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.MAIN_LOGIN_BUTTON)).click()
        # Кликаем по тексту ссылки восстановления пароля
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.LINK_TEXT, "Восстановить пароль"))).click()
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.FORGOT_PASSWORD_LOGIN_LINK)).click()
        login_user(driver, "maria_test_login@yandex.ru", "password123")
        assert WebDriverWait(driver, 8).until(EC.presence_of_element_located(StellarBurgersLocators.MAIN_ORDER_BUTTON)).is_displayed()


    # --- БЛОК 2: ПЕРЕХОД В ЛИЧНЫЙ КАБИНЕТ (1 ТЕСТ) ---

    def test_navigate_to_personal_account(self, driver):
        driver.get(StellarBurgersUrls.BASE_URL)
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.MAIN_LOGIN_BUTTON)).click()
        login_user(driver, "maria_test_login@yandex.ru", "password123")
        
        # Переходим в Личный кабинет
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.HEADER_PROFILE_BUTTON)).click()
        # Проверяем в ассерте, что URL изменился и содержит нужный эндпоинт
        assert WebDriverWait(driver, 8).until(EC.url_contains("/account"))


    # --- БЛОК 3: ПЕРЕХОД ИЗ ЛИЧНОГО КАБИНЕТА В КОНСТРУКТОР (2 ТЕСТА) ---

    # Переход по клику на кнопку «Конструктор»
    def test_navigate_from_account_to_constructor_via_button(self, driver):
        driver.get(StellarBurgersUrls.BASE_URL)
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.MAIN_LOGIN_BUTTON)).click()
        login_user(driver, "maria_test_login@yandex.ru", "password123")
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.HEADER_PROFILE_BUTTON)).click()
        
        # Возвращаемся в конструктор по верхней кнопке
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.HEADER_CONSTRUCTOR_BUTTON)).click()
        assert WebDriverWait(driver, 8).until(EC.presence_of_element_located(StellarBurgersLocators.MAIN_ORDER_BUTTON)).is_displayed()

    # Переход по клику на логотип «Stellar Burgers»
    def test_navigate_from_account_to_constructor_via_logo(self, driver):
        driver.get(StellarBurgersUrls.BASE_URL)
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.MAIN_LOGIN_BUTTON)).click()
        login_user(driver, "maria_test_login@yandex.ru", "password123")
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.HEADER_PROFILE_BUTTON)).click()
        
        # Возвращаемся в конструктор по клику на центральный логотип
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.HEADER_LOGO)).click()
        assert WebDriverWait(driver, 8).until(EC.presence_of_element_located(StellarBurgersLocators.MAIN_ORDER_BUTTON)).is_displayed()


    # --- БЛОК 4: ВЫХОД ИЗ АККАУНТА (1 ТЕСТ) ---

    def test_logout_from_personal_account(self, driver):
        driver.get(StellarBurgersUrls.BASE_URL)
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.MAIN_LOGIN_BUTTON)).click()
        login_user(driver, "maria_test_login@yandex.ru", "password123")
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.HEADER_PROFILE_BUTTON)).click()
        
        # Нажимаем кнопку «Выйти» в профиле
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.LOGOUT_BUTTON)).click()
        # Верифицируем, что система перенаправила нас обратно на страницу авторизации
        assert WebDriverWait(driver, 8).until(EC.url_contains("/login"))