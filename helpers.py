import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators

def generate_email():
    random_digits = random.randint(100, 999)
    return f"maria_popova_52_{random_digits}@yandex.ru"

def generate_password(length=6):
    return "".join(str(random.randint(0, 9)) for _ in range(length))

def login_user(driver, email, password):
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.LOGIN_EMAIL_INPUT)).send_keys(email)
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.LOGIN_PASSWORD_INPUT)).send_keys(password)
    driver.find_element(*StellarBurgersLocators.LOGIN_SUBMIT_BUTTON).click()