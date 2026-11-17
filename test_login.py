import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture
def driver():
    browser= webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()
def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"inventory_list")))
    assert "inventory" in driver.current_url


def test_invalid_login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID,"user-name").send_keys("wrong_username")
    driver.find_element(By.ID,"password").send_keys("wrong_password")
    driver.find_element(By.ID,"login-button").click()
    wait = WebDriverWait(driver, 10)
    error=wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='error']")))
    assert error.is_displayed()



