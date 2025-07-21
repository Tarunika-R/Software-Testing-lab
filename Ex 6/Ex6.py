from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the browser
driver = webdriver.Chrome()

# IMPORTANT: Use file:/// prefix for local files and fix backslashes or spaces if any in your path
file_path = "D:/TARU/V th year/Software Testing lab/Ex 6/calculator.html"
driver.get("file:///" + file_path.replace("\\", "/"))

def click_buttons(buttons):
    for btn in buttons:
        driver.find_element(By.XPATH, f"//button[text()='{btn}']").click()
    time.sleep(1)

def get_result():
    return driver.find_element(By.ID, "display").get_attribute("value")

def test_case(description, inputs, expected, operator_name=None):
    click_buttons(['C'])  # Clear before test
    click_buttons(inputs)
    result = get_result()

    # Build descriptive operator name if not passed
    if not operator_name:
        # map operator symbol to words
        op_map = {'+': 'Add', '-': 'Subtract', '*': 'Multiply', '/': 'Divide'}
        # find operator in inputs
        operator = next((ch for ch in inputs if ch in op_map), '?')
        operator_name = op_map.get(operator, operator)

    # Print formatted output
    test_expr = f"{inputs[0]} {operator_name} {inputs[2]} = {expected}"
    print(f"Test: {test_expr}")
    if result == expected:
        print("✅ Test Passed")
    else:
        print(f"❌ Test Failed - Expected: {expected}, Got: {result}")
    print("--------")

# Test cases with detailed output
test_case("Addition", ['7', '+', '3', '='], '10')
test_case("Multiplication", ['5', '*', '6', '='], '30')
test_case("Division", ['8', '/', '4', '='], '2')
test_case("Failed Test", ['9', '-', '4', '='], '6')  # Intentionally failing

driver.quit()
