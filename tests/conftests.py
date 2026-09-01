import random
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture
def generate_email():
    def _generate():
        random_digits = random.randint(100, 999)
        return f"maria_popova_52_{random_digits}@yandex.ru"
    return _generate

@pytest.fixture
def generate_password():
    def _generate(length=6):
        return "".join(str(random.randint(0, 9)) for _ in range(length))
    return _generate