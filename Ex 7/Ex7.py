from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

# Load local HTML file
file_path = os.path.abspath("college_form.html")
driver = webdriver.Chrome()  # Ensure chromedriver is in PATH
driver.get("file://" + file_path)

# Wait for page to load
time.sleep(1)

# Select Country
country_select = Select(driver.find_element(By.ID, "country"))
country_select.select_by_visible_text("India")
time.sleep(0.8)
selected_country = country_select.first_selected_option.text
assert selected_country == "India"
print("Country selected correctly:", selected_country)

# Select Category
category_select = Select(driver.find_element(By.ID, "category"))
category_select.select_by_visible_text("OBC")
time.sleep(0.8)
selected_category = category_select.first_selected_option.text
assert selected_category == "OBC"
print("Category selected correctly:", selected_category)

# Set Date of Birth
dob_input = driver.find_element(By.ID, "dob")
dob_input.send_keys("2000-01-01")
time.sleep(0.8)
print("DOB set.")

# Enter Email
email_input = driver.find_element(By.ID, "email")
email_input.send_keys("testuser@example.com")
time.sleep(0.8)
print("Email entered.")

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

# Submit Form
submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
time.sleep(1)
submit_button.click()
print("Form submitted.")

# Wait before closing
time.sleep(2)
driver.quit()
