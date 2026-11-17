import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture
def driver():
    browser=webdriver.Chrome()
    yield browser
    browser.quit()
@pytest.fixture
def logged_in_driver(driver):
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    driver.find_element(
        By.ID, "password"
    ).send_keys("secret_sauce")

    driver.find_element(
        By.ID, "login-button"
    ).click()

    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )

    return driver