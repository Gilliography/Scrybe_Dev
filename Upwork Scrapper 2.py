import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Define the URL for the Quora job search (modify as needed)
url = "https://www.quora.com/topic/Jobs-and-Careers"  # Adjust to the correct URL if available

# Headers to mimic a browser visit
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "DNT": "1"
}

# Setup retry session
session = requests.Session()
retry = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

# Function to scrape a page
def scrape_page(url):
    try:
        response = session.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Debugging: Print the first 500 characters of the HTML content
    print(soup.prettify()[:500])
    
    # Extract job listings (adjust selectors based on actual Quora structure)
    jobs = soup.find_all('div', class_='q-box qu-mb--tiny')  # Adjust selector based on actual HTML
    
    if not jobs:
        print("No job listings found. Check the HTML structure and selectors.")
    
    job_list = []
    
    for job in jobs:
        title = job.find('h2').get_text(strip=True) if job.find('h2') else 'N/A'
        company = 'N/A'  # Adjust based on actual structure
        location = 'N/A'  # Adjust based on actual structure
        job_url = job.find('a')['href'] if job.find('a') else 'N/A'
        
        job_list.append({
            'Title': title,
            'Company': company,
            'Location': location,
            'URL': job_url
        })
    
    return job_list

# Scrape multiple pages
def scrape_jobs(base_url):
    all_jobs = []
    page = 0  # Adjust page handling if needed
    
    while True:
        print(f"Scraping page {page + 1}")
        jobs = scrape_page(base_url + f"&page={page + 1}")
        if not jobs:
            break
        
        all_jobs.extend(jobs)
        page += 1
        time.sleep(5)  # Pause to prevent overwhelming the server
    
    return all_jobs

# Main
if __name__ == "__main__":
    jobs = scrape_jobs(url)
    df = pd.DataFrame(jobs)
    
    # Get the path to the Downloads folder
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    
    # Save the file in the Downloads folder
    df.to_excel(os.path.join(downloads_path, 'quora_jobs.xlsx'), index=False)
    
    print("Scraping complete. Data saved to 'quora_jobs.xlsx' in your Downloads folder.")


