from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager()
                                                  .install()))
driver.get("http://the-internet.herokuapp.com/login")
username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("tomsmith")
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("SuperSecretPassword!")
# Нажатие на кнопку "Login".
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()
sleep(2)
# Получение текста с зеленой плашки.
message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
print_message = message.text.strip()  # Удаление лишних пробелов
# и переводов строки.
print(print_message)

driver.quit()
