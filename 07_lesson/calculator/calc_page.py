from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def open(self):
        self.driver.get(self.url)

    def __init__(self, driver):
        self.driver = driver

    def do_calc(self, value):
        text_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        text_input.clear()
        text_input.send_keys(value)

    def click_button(self, button_text):
        button = self.driver.find_element(By.XPATH,
                                          f"//span[text()='{button_text}']")
        button.click()

    def wait(self):
        WebDriverWait(self.driver, 46).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".screen"))
        )
        WebDriverWait(self.driver, 46).until(
            EC.text_to_be_present_in_element
            ((By.CSS_SELECTOR, ".screen"), "15")
        )

    def get_result(self):
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return result
