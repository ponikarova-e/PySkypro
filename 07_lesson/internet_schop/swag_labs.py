from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SwagLabs:
    def __init__(self, driver):
        self.driver = driver

    def fill_in_form(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, 'first-name').send_keys(first_name)
        self.driver.find_element(By.ID, 'last-name').send_keys(last_name)
        self.driver.find_element(By.ID, 'postal-code').send_keys(postal_code)
        continue_button = self.driver.find_element(By.ID, 'continue')
        continue_button.click()

    # Читаем итоговую сумму
    def get_total_price(self):
        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, 'summary_total_label')))
        total_text = total_element.text  # например: "Total: $58.29"
        total_value = total_text.split('$')[-1]
        return total_value
