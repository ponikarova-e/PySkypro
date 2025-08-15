from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalcPage:
    """
    Класс для взаимодействия со страницей калькулятора.
    """

    url: str = ("https://bonigarcia.dev"
                "/selenium-webdriver-java/slow-calculator.html")

    def __init__(self, driver):
        """
        Инициализация объекта страницы.

        :param driver: webdriver.Chrome - экземпляр драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
        Открывает страницу калькулятора в браузере.

        :return: None
        """
        self.driver.get(self.url)

    @allure.step("Ввод значения '{value}' в текстовое поле")
    def do_calc(self, value: str) -> None:
        """
        Вводит значение в текстовое поле с задержкой.

        :param value: str - значение для ввода.
        :return: None
        """
        text_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        text_input.clear()
        text_input.send_keys(value)

    @allure.step("Нажатие кнопки с текстом '{button_text}'")
    def click_button(self, button_text: str) -> None:
        """
        Нажимает кнопку по её тексту.

        :param button_text: str - текст кнопки.
        :return: None
        """
        button = self.driver.find_element(By.XPATH,
                                          f"//span[text()='{button_text}']")
        button.click()

    @allure.step("Ожидание результата и проверка отображения числа '15'")
    def wait(self) -> None:
        """
        Ожидает появления результата и появления числа '15' на экране.

        :return: None
        """
        WebDriverWait(self.driver, 46).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".screen"))
        )
        WebDriverWait(self.driver, 46).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"),
                                             "15")
        )

    @allure.step("Получение текста результата")
    def get_result(self) -> str:
        """
        Получает текущий результат из элемента с классом 'screen'.

        :return: str - текст результата.
        """
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return result
