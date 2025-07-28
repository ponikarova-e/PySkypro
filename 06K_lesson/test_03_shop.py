from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_internet_shop():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait = WebDriverWait(driver, 10)

    # Добавляем товары в корзину
    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for product_name in products:
        # Находим карточку товара по названию и добавляем в корзину
        product_xpath = (f"//div[text()='{product_name}']"
                         f"/ancestor::div[@class='inventory_item']//button")
        add_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, product_xpath)))
        add_button.click()

    # Переходим в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Нажимаем Checkout
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # Заполняем форму
    wait.until(EC.element_to_be_clickable(
        (By.ID, "first-name"))).send_keys("ВашеИмя")
    driver.find_element(By.ID, "last-name").send_keys("ВашаФамилия")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    # Читаем итоговую сумму
    total_element = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label")))
    total_text = total_element.text  # Например: "Total: $58.29"

    print("Итоговая стоимость:", total_text)

    total = float(total_text.split("$")[-1])
    # Извлечь число из "Total: $58.29"
    assert total == 58.29

    WebDriverWait(driver, 10)
    driver.quit()
