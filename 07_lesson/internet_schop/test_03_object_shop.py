from selenium import webdriver
from authorization_shop import Authorization
from home_page_shop import HomePage
from basket import Basket
from swag_labs import SwagLabs


def test_internet_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')
    driver.implicitly_wait(4)
    page_aut = Authorization(driver)
    page_aut.login('standard_user', 'secret_sauce')
    home_pro = HomePage(driver)
    products_to_add = [
        'Sauce Labs Backpack',
        'Sauce Labs Bolt T-Shirt',
        'Sauce Labs Onesie'
    ]
    for product in products_to_add:
        home_pro.search_product(product)
    main_basket = Basket(driver)
    main_basket.go_to_cart()
    main_basket.checout()
    main_form = SwagLabs(driver)
    main_form.fill_in_form("ВашеИмя", "ВашаФамилия", "12345")
    total_form = main_form.get_total_price()

    assert total_form == '58.29'
    driver.quit()
