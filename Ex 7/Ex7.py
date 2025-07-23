from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

# Load local HTML file
file_path = os.path.abspath("college_form.html")
driver = webdriver.Chrome()
driver.get("file://" + file_path)

time.sleep(1)

# Select Country
country_select = Select(driver.find_element(By.ID, "country"))
country_select.select_by_visible_text("India")
time.sleep(0.8)
assert country_select.first_selected_option.text == "India"
print("Country selected correctly.")

# Select Category
category_select = Select(driver.find_element(By.ID, "category"))
category_select.select_by_visible_text("OBC")
time.sleep(0.8)
assert category_select.first_selected_option.text == "OBC"
print("Category selected correctly.")

# Set DOB
dob_input = driver.find_element(By.ID, "dob")
dob_input.send_keys("01-01-2000")
time.sleep(0.8)
print("DOB set.")

# Enter Email (Intentionally wrong)
email_input = driver.find_element(By.ID, "email")
invalid_email = "testuserexample.com"  # no '@'
email_input.send_keys(invalid_email)
time.sleep(0.8)

# Email validation assertion (purposeful fail)
try:
    assert "@" in invalid_email
    print("Email entered correctly.")
except AssertionError:
    print("Email NOT correct ❌ — Skipping form submission.")
    driver.quit()
    exit()

# Select Qualification
qualification_select = Select(driver.find_element(By.ID, "qualification"))
qualification_select.select_by_visible_text("Bachelor")
time.sleep(0.8)
assert qualification_select.first_selected_option.text == "Bachelor"
print("Qualification selected correctly.")

# Select Course
course_select = Select(driver.find_element(By.ID, "course"))
course_select.select_by_visible_text("MBA")
time.sleep(0.8)
assert course_select.first_selected_option.text == "MBA"
print("Course selected correctly.")

# Submit Form (won't reach here if email failed)
submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
time.sleep(1)
submit_button.click()
print("Form submitted.")

time.sleep(2)
driver.quit()
