from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import threading

# Set up Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Define the search URL
search_query = 'https://gtaforums.com/'
search_url = f'https://www.webcrawler.com/search/web?q={search_query.replace(" ", "+")}'

# Function to extract search results from a page
def extract_search_results(driver):
    data = []
    results = driver.find_elements(By.CSS_SELECTOR, '.web-yahoo-wrap')  # Adjust selector based on WebCrawler's HTML structure
    for result in results:
        title = result.text.strip()
        link = result.get_attribute('href')
        data.append([title, link])
    return data

# Function to check for Cloudflare verification page
def is_cloudflare_verification_page():
    try:
        cloudflare_text = driver.find_element(By.XPATH, '//title[contains(text(), "Attention Required")]')
        return True
    except:
        return False

# Function to automatically close Cloudflare verification after a timeout
def close_cloudflare_verification_after_timeout():
    print("Waiting for Cloudflare verification page to close automatically...")
    time.sleep(30)  # Adjust timeout period as needed
    driver.switch_to.alert.accept()  # Example: Assuming Cloudflare verification closes via alert

# Navigate to the search URL
driver.get(search_url)
time.sleep(5)  # Wait for the page to load

all_data = []

# Loop to handle pagination
while True:
    # Check for Cloudflare verification page
    if is_cloudflare_verification_page():
        print("Cloudflare verification detected. Waiting for verification to complete manually...")
        threading.Thread(target=close_cloudflare_verification_after_timeout).start()  # Start timer thread

        input("Press Enter after completing the verification...")
        print("Verification completed.")

    # Extract data from the current page
    all_data.extend(extract_search_results(driver))
    
    try:
        # Find and click the "Next" button
        next_button = driver.find_element(By.LINK_TEXT, 'Next')
        next_button.click()
        time.sleep(5)  # Wait for the next page to load
    except:
        # If no "Next" button is found, break the loop
        break

# Close the WebDriver
driver.quit()

# Create a DataFrame using pandas
df = pd.DataFrame(all_data, columns=['Title', 'Link'])

# Save the DataFrame to a CSV file
df.to_csv('2.csv', index=False)

print('Data has been saved to webcrawler_search_results.csv')
