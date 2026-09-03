from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators
from urls import StellarBurgersUrls 
from helpers import generate_email, generate_password

def test_successful_registration(driver):
    driver.get(StellarBurgersUrls.BASE_URL)
    # Клик на главной: "Войти в аккаунт"
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.MAIN_LOGIN_BUTTON)).click()
    # Клик на странице входа: "Зарегистрироваться" (исправленный локатор)
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.LOGIN_REG_LINK)).click()

    # Заполнение формы регистрации
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.REG_NAME_INPUT)).send_keys("Мария")
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.REG_EMAIL_INPUT)).send_keys(generate_email())
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.REG_PASSWORD_INPUT)).send_keys(generate_password(6))
    driver.find_element(*StellarBurgersLocators.REG_SUBMIT_BUTTON).click()

    assert WebDriverWait(driver, 8).until(EC.url_contains("/login"))

def test_registration_with_short_password_error(driver):
    driver.get(StellarBurgersUrls.BASE_URL)
    # Клик на главной: "Войти в аккаунт"
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.MAIN_LOGIN_BUTTON)).click()
    # Клик на странице входа: "Зарегистрироваться" (исправленный локатор)
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.LOGIN_REG_LINK)).click()

    # Заполнение формы с коротким паролем
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.REG_NAME_INPUT)).send_keys("Мария")
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.REG_EMAIL_INPUT)).send_keys(generate_email())
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.REG_PASSWORD_INPUT)).send_keys(generate_password(5))
    driver.find_element(*StellarBurgersLocators.REG_SUBMIT_BUTTON).click()

    # Проверка сообщения об ошибке
    assert WebDriverWait(driver, 8).until(
        EC.presence_of_element_located(StellarBurgersLocators.REG_PASSWORD_ERROR)
    ).is_displayed()
