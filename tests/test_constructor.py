from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators
from urls import StellarBurgersUrls  # Добавила импорт из нового файла! 

class TestStellarBurgersConstructor:

    # 1. Тест перехода на вкладку «Соусы»
    def test_constructor_switch_to_sauces_tab(self, driver):
        driver.get(StellarBurgersUrls.BASE_URL)
        
        # Сразу находим контейнер вкладки
        tab_sauces = WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.TAB_SAUCES_CONTAINER))
        tab_sauces.click()
        
        # Кристально чистый ассерт без By.XPATH — считываем класс напрямую у контейнера!
        assert "tab_type_current" in tab_sauces.get_attribute("class")

    # 2. Тест перехода на вкладку «Начинки»
    def test_constructor_switch_to_fillings_tab(self, driver):
        driver.get(StellarBurgersUrls.BASE_URL)
        
        tab_fillings = WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.TAB_FILLINGS_CONTAINER))
        tab_fillings.click()
        
        assert "tab_type_current" in tab_fillings.get_attribute("class")

    # 3. Тест возврата на вкладку «Булки»
    def test_constructor_switch_to_buns_tab(self, driver):
        driver.get(StellarBurgersUrls.BASE_URL)
        
        tab_sauces = WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.TAB_SAUCES_CONTAINER))
        tab_buns = WebDriverWait(driver, 8).until(EC.element_to_be_clickable(StellarBurgersLocators.TAB_BUNS_CONTAINER))
        
        # Кликаем на соусы, а затем возвращаемся на булки
        tab_sauces.click()
        tab_buns.click()
        
        assert "tab_type_current" in tab_buns.get_attribute("class")