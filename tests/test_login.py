from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators

def register_user_for_login(driver, email, password):
    driver.get("https://stellarburgers.education-services.ru")
    
    # Явные ожидания БЕЗ звёздочки для element_to_be_clickable
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.REG_NAME_INPUT)).send_keys("Мария")
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.REG_EMAIL_INPUT)).send_keys(email)
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.REG_PASSWORD_INPUT)).send_keys(password)
    
    driver.find_element(*StellarBurgersLocators.REG_SUBMIT_BUTTON).click()
    WebDriverWait(driver, 8).until(EC.url_to_be("https://stellarburgers.education-services.ru"))

def login_and_verify(driver, email, password):
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.LOGIN_EMAIL_INPUT)).send_keys(email)
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.LOGIN_PASSWORD_INPUT)).send_keys(password)
    
    driver.find_element(*StellarBurgersLocators.LOGIN_SUBMIT_BUTTON).click()
    WebDriverWait(driver, 8).until(EC.url_to_be("https://stellarburgers.education-services.ru"))
    assert driver.current_url == "https://stellarburgers.education-services.ru"

def test_login_from_main_page_button(driver, generate_email, generate_password):
    email = generate_email()
    password = generate_password()
    register_user_for_login(driver, email, password)
    
    driver.get("https://stellarburgers.education-services.ru")
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.MAIN_LOGIN_BUTTON)).click()
    login_and_verify(driver, email, password)

def test_login_from_header_profile_button(driver, generate_email, generate_password):
    email = generate_email()
    password = generate_password()
    register_user_for_login(driver, email, password)
    
    driver.get("https://stellarburgers.education-services.ru")
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.HEADER_PROFILE_BUTTON)).click()
    login_and_verify(driver, email, password)

def test_login_from_registration_page_link(driver, generate_email, generate_password):
    email = generate_email()
    password = generate_password()
    register_user_for_login(driver, email, password)
    
    driver.get("https://stellarburgers.education-services.ru")
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.REG_LOGIN_LINK)).click()
    login_and_verify(driver, email, password)

def test_login_from_forgot_password_page_link(driver, generate_email, generate_password):
    email = generate_email()
    password = generate_password()
    register_user_for_login(driver, email, password)
    
    driver.get("https://stellarburgers.education-services.ruforgot-password")
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.FORGOT_PASSWORD_LOGIN_LINK)).click()
    login_and_verify(driver, email, password)