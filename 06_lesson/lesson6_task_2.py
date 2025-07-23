from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager()
                                                .install()))
driver.get("http://uitestingplayground.com/textinput")
element = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
element.send_keys("SkyPro")
sleep(3)
button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
sleep(5)
update_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
txt = update_button.text
print(txt)

driver.quit()
