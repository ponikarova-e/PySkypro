from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def search_product(self, product_name):
        # Находим карточку товара по названию и добавляем в корзину
        product_xpath = (f"//div[text()='{product_name}']"
                         f"/ancestor::div[@class='inventory_item']//button")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, product_xpath))).click()
