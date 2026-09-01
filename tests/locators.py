from selenium.webdriver.common.by import By

class StellarBurgersLocators:
    # --- СТРАНИЦА РЕГИСТРАЦИИ ---
    REG_NAME_INPUT = (By.CSS_SELECTOR, "fieldset:nth-child(1) input") # Первое поле ввода (Имя)
    REG_EMAIL_INPUT = (By.CSS_SELECTOR, "fieldset:nth-child(2) input") # Второе поле ввода (Email)
    REG_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    REG_SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    REG_PASSWORD_ERROR = (By.XPATH, ".//p[text()='Некорректный пароль']")
    REG_LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")

    # --- СТРАНИЦА ВХОДА (АВТОРИЗАЦИИ) ---
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='text']")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Войти']")

    # --- ГЛАВНАЯ СТРАНИЦА ---
    MAIN_LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    HEADER_PROFILE_BUTTON = (By.XPATH, ".//p[text()='Личный кабинет']")
    HEADER_CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    HEADER_LOGO = (By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]")
    MAIN_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")

    # --- СТРАНИЦА ВОССТАНОВЛЕНИЯ ПАРОЛЯ ---
    FORGOT_PASSWORD_LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")