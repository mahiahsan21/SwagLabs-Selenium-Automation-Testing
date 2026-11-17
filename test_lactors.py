
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://www.saucedemo.com/")

    # 1. Find username using ID
    username = driver.find_element(By.ID, "user-name")
    print("Username field:", username.is_displayed())

    # 2. Find password using NAME
    password = driver.find_element(By.NAME, "password")
    print("Password field:", password.is_displayed())

    # 3. Find login using CSS selector
    login = driver.find_element(
        By.CSS_SELECTOR, "[data-test='login-button']"
    )
    print("Login button:", login.is_displayed())

    # 4. Find username using XPath
    username_xpath = driver.find_element(
        By.XPATH, "//input[@data-test='username']"
    )
    print("XPath username:", username_xpath.is_displayed())

    # 5. Validate the elements
    assert username.is_displayed()
    assert password.is_displayed()
    assert login.is_displayed()
    assert username_xpath.is_displayed()

    print("ALL LOCATOR TESTS PASSED")

finally:
    driver.quit()
