from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options to use the remote debugging port
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
print("Chrome options set")

# Initialize the driver with the existing session
driver = webdriver.Chrome(options=chrome_options)
print(driver)
try:
    # Navigate to the course registration page (assuming you're already logged in)
    driver.get("https://auris.ahduni.edu.in/core-emli/code/student_portal/_CourseRegistration_monsoon2024.php")

    # Perform your automated tasks here
    # Wait until the page loads
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "My Courses")))

    # Search for the course
    search_box = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
    search_box.send_keys("BIO213")
    search_box.send_keys(Keys.RETURN)

    # Wait for search results to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "BIO213 Basics of Bioinformatics")))

    # Select the desired schedule
    radio_button = driver.find_element(By.ID, "RadioSch_2255")  # Update the ID as needed
    radio_button.click()

    # Check for clashes and add the course
    add_course_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "TrtableButtonID-2255-2255")))
    add_course_button.click()

    # Additional steps can be added as needed

finally:
    # Optional: Close the driver
    driver.quit()

    