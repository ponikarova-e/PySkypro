import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestFormSubmission:

    @pytest.fixture(scope='class')
    def setup(self):
        # Указываем какой браузер использовать
        self.driver =webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        yield
        self.driver.quit()

    def test_form_submission(self, setup):
        # Заполним форму
        self.driver.find_element(By.NAME, "firstname").send_keys("Иван")
        self.driver.find_element(By.NAME, "lastname").send_keys("Петров")
        self.driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        self.driver.find_element(By.NAME, "email").send_keys("test@skypro.com")
        self.driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        self.driver.find_element(By.NAME, "zipcode").send_keys("")  # Оставим пустым
        self.driver.find_element(By.NAME, "city").send_keys("Москва")
        self.driver.find_element(By.NAME, "country").send_keys("Россия")
        self.driver.find_element(By.NAME, "job").send_keys("QA")
        self.driver.find_element(By.NAME, "company").send_keys("SkyPro")

        # Нажимаем кнопку Submit
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        # Ожидаем, пока все поля будут проверены
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".component"))
        )

        # Проверим, что поле Zip code подсвечено красным
        zip_code_field = self.driver.find_element(By.NAME, "zipcode")
        zip_code_border_color = zip_code_field.value_of_css_property('border-color')
        assert "rgb(255, 0, 0)" in zip_code_border_color, f"Expected Zip code to have red border, but got {zip_code_border_color}"

        # Проверим, что остальные поля подсвечены зеленым
        fields = [
            "firstname", "lastname", "address", "email",
            "phone", "city", "country", "job", "company"
        ]

        for field_name in fields:
            field = self.driver.find_element(By.NAME, field_name)
            border_color = field.value_of_css_property('border-color')
            assert "rgb(0, 128, 0)" in border_color, f"Expected {field_name} to have green border, but got {border_color}"