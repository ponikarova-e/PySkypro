from selenium import webdriver
from calc_page import CalcPage


def test_calc():
    driver = webdriver.Chrome()
    calculator = CalcPage(driver)
    calculator.open()
    calculator.do_calc("45")
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")
    calculator.wait()
    result = calculator.get_result()
    assert result == "15"
