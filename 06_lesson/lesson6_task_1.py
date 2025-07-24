from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#  from time import sleep


driver = (webdriver.Chrome
          (service=ChromeService(ChromeDriverManager().install())))
driver.get("http://uitestingplayground.com/ajax")
element = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
wait = WebDriverWait(driver, 17)
button = wait.until(EC.text_to_be_present_in_element
                    ((By.CSS_SELECTOR, "#content"),
                     "Data loaded with AJAX get request."))

txt = driver.find_element(By.CSS_SELECTOR, "#content").text
print(txt)

driver.quit()
