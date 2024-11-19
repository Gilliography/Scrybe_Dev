import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Chrome WebDriver (make sure to provide the correct path to your downloaded WebDriver)
driver_path = '/path/to/chromedriver'  # Update with your ChromeDriver path
driver = webdriver.Chrome(executable_path=driver_path)

# Define the URL for the Crunchbase search
url = 'https://www.crunchbase.com/search/organizations/field/organizations/industries/information-technology/location/texas'

# Load the webpage
driver.get(url)

# Allow time for the page to fully load
time.sleep(5)

# Extract company names (adjust the HTML tags as needed for the website)
company_list = []
company_elements = driver.find_elements(By.CLASS_NAME, 'organization_title')

for company in company_elements:
    company_name = company.text.strip()
    company_list.append(company_name)

# Close the browser after scraping
driver.quit()

# Save the scraped data to an Excel file
df = pd.DataFrame(company_list, columns=['Company Name'])

# Define the file path where you want to save the Excel file (change this to your preferred path)
file_path = os.path.join(os.path.expanduser("~"), 'Downloads', 'Texas_IT_Companies.xlsx')

# Save the DataFrame to Excel
df.to_excel(file_path, index=False)

print(f"Excel file has been downloaded and saved to {file_path}")
