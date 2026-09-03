from selenium.webdriver.common.by import By

class StellarBurgersLocators:
    # --- СТРАНИЦА РЕГИСТРАЦИИ ---
    REG_NAME_INPUT = (By.CSS_SELECTOR, "fieldset:nth-child(1) input")
    REG_EMAIL_INPUT = (By.CSS_SELECTOR, "fieldset:nth-child(2) input")
    REG_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    REG_SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    REG_PASSWORD_ERROR = (By.XPATH, ".//p[text()='Некорректный пароль']")
    REG_LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")

    # --- СТРАНИЦА ВХОДА (АВТОРИЗАЦИИ) ---
    # ИСПРАВЛЕНО: Заменили неработающие CSS/XPath на надежный поиск по атрибуту name
    LOGIN_EMAIL_INPUT = (By.XPATH, ".//input[@name='name']")
    LOGIN_PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']")
    
    LOGIN_SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    LOGIN_REG_LINK = (By.XPATH, ".//a[text()='Зарегистрироваться']")
    
    # ДОБАВЛЕНО: Локатор для перехода на страницу восстановления пароля из формы входа
    LOGIN_FORGOT_PASSWORD_LINK = (By.XPATH, ".//a[@href='/forgot-password']")

    # --- ГЛАВНАЯ СТРАНИЦА ---
    MAIN_LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    HEADER_PROFILE_BUTTON = (By.XPATH, ".//a[@href='/account']")
    HEADER_CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    # ИСПРАВЛЕНО: Добавили поиск ссылки внутри блока логотипа, чтобы клик не уходил в пустоту
    HEADER_LOGO = (By.XPATH, ".//div[contains(@class, 'AppHeader_header_logo')]//a")
    MAIN_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")

    # --- НОВЫЕ ЛОКАТОРЫ ДЛЯ ВЫХОДА И ВКЛАДОК КОНСТРУКТОРA ---
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выйти']")
    TAB_BUNS_CONTAINER = (By.XPATH, ".//span[text()='Булки']/..")
    TAB_SAUCES_CONTAINER = (By.XPATH, ".//span[text()='Соусы']/..")
    TAB_FILLINGS_CONTAINER = (By.XPATH, ".//span[text()='Начинки']/..")

    # --- СТРАНИЦА ВОССТАНОВЛЕНИЯ ПАРОЛЯ ---
    FORGOT_PASSWORD_LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")

