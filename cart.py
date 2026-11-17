import pytest
from cffi.cffi_opcode import CLASS_NAME
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Start Chrome

def test_add_items(logged_in_driver):
    driver = logged_in_driver
    wait= WebDriverWait(driver,10)
    driver.find_element(By.CSS_SELECTOR,"[data-test='add-to-cart-sauce-labs-backpack']").click()
    badge=wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge")))
    assert badge.text=="1"

def test_add_multiple_cart(logged_in_driver):

    driver = logged_in_driver

    wait = WebDriverWait(driver, 10)

    products = [
    "sauce-labs-bike-light",
    "sauce-labs-backpack",
    "sauce-labs-onesie",
    "sauce-labs-bolt-t-shirt",
    "sauce-labs-fleece-jacket",
    "test.allthethings()-t-shirt-(red)"
    ]

    for product in products:

        button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 f"[data-test='add-to-cart-{product}']")
            )
        )

        button.click()

    # Verify cart badge
    badge = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert badge.text == "6"

   

    # Open cart
    driver.find_element(
        By.CLASS_NAME, "shopping_cart_link"
    ).click()

    # Debugging
    print("Current URL:", driver.current_url)
    print("Page title:", driver.title)

    # Check whether cart container exists
    print("Cart containers:",
          len(driver.find_elements(By.ID, "cart_contents_container")))

    # Check cart item elements
    print("Cart items:",
          len(driver.find_elements(By.CLASS_NAME, "cart_item")))

    # Wait for cart items
    cart_items = wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "cart_item")
        )
    )

    expected_products = [

        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)"
]



    actual_products = [
        item.find_element(
            By.CLASS_NAME, "inventory_item_name"
        ).text
        for item in cart_items
    ]

    assert sorted(actual_products) == sorted(expected_products)

    print("PASS: All six products added correctly")
def test_continue_btn(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
    #open cart link
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    continue_button= wait.until(EC.element_to_be_clickable((By.ID,"continue-shopping")))
    continue_button.click()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
    assert "inventory" in driver.current_url
    assert driver.find_element(By.CLASS_NAME,"inventory_list").is_displayed()
    print("pass: continue check button")
def test_checkout(logged_in_driver):
    driver=logged_in_driver
    wait= WebDriverWait(driver,10)
    #add_product
    driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
    # open cart link
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    checkout_button = wait.until(EC.element_to_be_clickable((By.ID,"checkout")))
    checkout_button.click()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"checkout_info_container")))
    assert "checkout" in driver.current_url
    assert driver.find_element(By.CLASS_NAME,"checkout_info_container").is_displayed()
    assert driver.find_element(By.ID,"first-name").is_displayed()
    assert driver.find_element(By.ID,"last-name").is_displayed()
    assert driver.find_element(By.ID,"postal-code").is_displayed()















