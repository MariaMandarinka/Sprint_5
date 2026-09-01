from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators

# 1. Тест успешной регистрации
def test_successful_registration(driver, generate_email, generate_password):
    # Открываем страницу регистрации
    driver.get("https://stellarburgers.education-services.ru")
    
    # Ожидаем загрузки полей и вводим данные (для element_to_be_clickable передаём локатор целиком)
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.REG_NAME_INPUT)).send_keys("Мария")
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.REG_EMAIL_INPUT)).send_keys(generate_email())
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.REG_PASSWORD_INPUT)).send_keys(generate_password(6))
    
    # Кликаем по кнопке отправки формы
    driver.find_element(*StellarBurgersLocators.REG_SUBMIT_BUTTON).click()
    
    # Ждем перехода на страницу входа
    WebDriverWait(driver, 8).until(EC.url_to_be("https://stellarburgers.education-services.ru"))
    assert driver.current_url == "https://stellarburgers.education-services.ru"

# 2. Тест ошибки короткого пароля (меньше 6 символов)
def test_registration_with_short_password_error(driver, generate_email, generate_password):
    driver.get("https://stellarburgers.education-services.ru")
    
    # Заполняем данные, но пароль запрашиваем длиной 5 символов
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.REG_NAME_INPUT)).send_keys("Мария")
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.REG_EMAIL_INPUT)).send_keys(generate_email())
    WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.REG_PASSWORD_INPUT)).send_keys(generate_password(5))
    
    driver.find_element(*StellarBurgersLocators.REG_SUBMIT_BUTTON).click()
    
    # Проверяем, что на экране появилось предупреждение об ошибке
    error_message = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located(StellarBurgersLocators.REG_PASSWORD_ERROR)
    )
    assert error_message.is_displayed()