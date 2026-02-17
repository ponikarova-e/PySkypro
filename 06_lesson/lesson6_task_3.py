from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager()
                                                .install()))
driver.get("https://bonigarcia.dev/selenium-webdriver"
           "-java/loading-images.html")
try:
    # Переход на страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver"
               "-java/loading-images.html")

    images = (WebDriverWait(driver, 20)
              .until(EC.text_to_be_present_in_element
              ((By.TAG_NAME, 'p'), "Done!")))

    print(driver.find_element
          (By.CSS_SELECTOR, "#award").get_dom_attribute("src"))

finally:
    driver.quit()
