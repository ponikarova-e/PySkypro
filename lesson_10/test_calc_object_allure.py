import allure
from selenium import webdriver
from calc_page_allure import CalcPage


@allure.title("Тест калькулятора для проверки сложения")
@allure.description("""
Этот тест открывает страницу калькулятора,
вводит значение 45, выполняет операцию 7 + 8,
и проверяет, что результат равен 15.
""")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc():
    """
    Основной тест для проверки работы калькулятора.

    Создает экземпляр драйвера и страницы,
    выполняет последовательность действий и проверяет результат.

    :return: None
    """

    # Инициализация драйвера Chrome
    with allure.step("Запуск драйвера Chrome"):
        driver = webdriver.Chrome()

    calculator = CalcPage(driver)

    try:
        # Открытие страницы калькулятора
        with allure.step("Открытие страницы калькулятора"):
            calculator.open()

        # Ввод значения 45 в поле задержки
        with allure.step("Ввод значения '45' в поле задержки"):
            calculator.do_calc("45")

        # Нажатие кнопки '7'
        with allure.step("Нажатие кнопки '7'"):
            calculator.click_button("7")

        # Нажатие кнопки '+'
        with allure.step("Нажатие кнопки '+'"):
            calculator.click_button("+")

        # Нажатие кнопки '8'
        with allure.step("Нажатие кнопки '8'"):
            calculator.click_button("8")

        # Нажатие кнопки '=' для вычисления результата
        with allure.step("Нажатие кнопки '=' для вычисления результата"):
            calculator.click_button("=")

        # Ожидание результата и его отображения
        with allure.step("Ожидание отображения результата '15'"):
            calculator.wait()

        # Получение результата из поля экрана
        with allure.step("Получение результата из поля экрана"):
            result = calculator.get_result()

        # Проверка соответствия результата ожидаемому значению '15'
        with allure.step(f"Проверка, что результат равен '15',"
                         f" полученное значение: {result}"):
            assert result == "15", (f"Ожидался результат '15',"
                                    f" получено '{result}'")

    finally:
        # Закрытие браузера после завершения теста
        with allure.step("Закрытие браузера"):
            driver.quit()
