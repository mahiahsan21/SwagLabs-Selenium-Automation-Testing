
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_complete_checkout_flow(logged_in_driver):

    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)

    # STEP 1: Add two products
    products = [
        "sauce-labs-backpack",
        "sauce-labs-bike-light"
    ]

    for product in products:
        button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 f"[data-test='add-to-cart-{product}']")
            )
        )
        button.click()

    # STEP 2: Verify cart badge
    badge = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert badge.text == "2"

    # STEP 3: Open cart
    driver.find_element(
        By.CLASS_NAME, "shopping_cart_link"
    ).click()

    cart_items = wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "cart_item")
        )
    )

    assert len(cart_items) == 2

    # STEP 4: Proceed to checkout
    driver.find_element(By.ID, "checkout").click()

    # STEP 5: Fill customer information
    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "first-name")
        )
    ).send_keys("Mahi")

    driver.find_element(By.ID, "last-name").send_keys("Ahsan")
    driver.find_element(By.ID, "postal-code").send_keys("1216")

    driver.find_element(By.ID, "continue").click()

    # STEP 6: Verify checkout overview
    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "checkout_summary_container")
        )
    )

    assert "checkout-step-two" in driver.current_url

    # STEP 7: Verify overview has two products
    overview_items = driver.find_elements(
        By.CLASS_NAME, "cart_item"
    )

    assert len(overview_items) == 2

    # STEP 8: Finish order
    driver.find_element(By.ID, "finish").click()

    # STEP 9: Verify order confirmation
    confirmation = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "complete-header")
        )
    )

    assert "Thank you for your order!" in confirmation.text

    print("PASS: Complete checkout integration test")
