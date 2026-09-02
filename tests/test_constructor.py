from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators, StellarBurgersUrls

class TestStellarBurgersConstructor:

    # Тест раздела «Конструктор» (Переключение вкладок: Булки, Соусы, Начинки)
    def test_constructor_tabs_switching(self, driver):
        # Открываем главную страницу (авторизация не требуется!)
        driver.get(StellarBurgersUrls.BASE_URL)
        
        # Находим элементы вкладок по нашим локаторам из файла locators.py
        tab_sauces = WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.TAB_SAUCES))
        tab_fillings = WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.TAB_FILLINGS))
        tab_buns = WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.TAB_BUNS))
        
        # 1. Кликаем на «Соусы» и проверяем, что вкладка стала активной
        tab_sauces.click()
        assert "tab_type_current" in tab_sauces.find_element(By.XPATH, "./..").get_attribute("class")
        
        # 2. Кликаем на «Начинки» и проверяем активность
        tab_fillings.click()
        assert "tab_type_current" in tab_fillings.find_element(By.XPATH, "./..").get_attribute("class")
        
        # 3. Возвращаемся на «Булки» и проверяем активность
        tab_buns.click()
        assert "tab_type_current" in tab_buns.find_element(By.XPATH, "./..").get_attribute("class")