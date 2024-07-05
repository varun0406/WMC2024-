import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the base URL of the website you want to scrape
BASE_URL = 'https://gtanet.com/'

# Function to fetch and parse a single page
def fetch_page(url):
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    return BeautifulSoup(response.content, 'html.parser')

# Function to extract data from a section of the page
def extract_section_data(section):
    data = []
    for item in section.select('.item-class'):  # Use the appropriate CSS selector
        title = item.select_one('.title-class').get_text(strip=True)
        description = item.select_one('.description-class').get_text(strip=True)
        date = item.select_one('.date-class').get_text(strip=True)
        data.append([title, description, date])
    return data

# Function to handle pagination and scrape all pages
def scrape_all_pages(base_url, total_pages):
    all_data = []
    for page in range(1, total_pages + 1):
        url = f'{base_url}/page/{page}'
        soup = fetch_page(url)
        sections = soup.select('.section-class')  # Adjust according to the site's structure
        for section in sections:
            section_data = extract_section_data(section)
            all_data.extend(section_data)
    return all_data

# Define the total number of pages to scrape (this might require prior inspection)
TOTAL_PAGES = 5

# Scrape all pages
scraped_data = scrape_all_pages(BASE_URL, TOTAL_PAGES)

# Create a DataFrame using pandas
df = pd.DataFrame(scraped_data, columns=['Title', 'Description', 'Date'])

# Save the DataFrame to a CSV file
df.to_csv('scraped_data.csv', index=False)

print('Data has been saved to scraped_data.csv')
