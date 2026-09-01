import time
from selenium import webdriver

# Запускаем браузер Chrome
driver = webdriver.Chrome()

# Открываем главную страницу Google
driver.get("https://google.com")

# Ждем 5 секунд, чтобы вы успели увидеть окно браузера
time.sleep(5)

# Закрываем браузер автоматикой
driver.quit()