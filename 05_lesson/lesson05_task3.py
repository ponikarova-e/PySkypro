from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager()
                                                  .install()))
driver.get("http://the-internet.herokuapp.com/inputs")
# Находим поле ввода по тегу input
input_field = driver.find_element(By.TAG_NAME, "input")
sleep(5)
# Вводим текст "Sky"
input_field.send_keys("Sky")

# Очищаем поле
input_field.clear()
sleep(5)
# Вводим текст "Pro"
input_field.send_keys("Pro")

sleep(5)

driver.quit()
