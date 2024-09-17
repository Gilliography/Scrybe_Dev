import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

# Define the URL for the Upwork job search
url = "https://www.upwork.com/ab/jobs/search/?q=full-time&sort=recency"

# Headers to mimic a browser visit (some websites may block requests without this)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Function to scrape a page
def scrape_page(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract job listings (adjust selectors based on actual Upwork structure)
    jobs = soup.find_all('section', class_='job-tile')
    
    job_list = []
    
    for job in jobs:
        title = job.find('h4').get_text(strip=True)
        company = job.find('span', class_='company-name').get_text(strip=True)
        location = job.find('span', class_='job-location').get_text(strip=True)
        job_url = job.find('a')['href']
        
        job_list.append({
            'Title': title,
            'Company': company,
            'Location': location,
            'URL': f"https://www.upwork.com{job_url}"
        })
    
    return job_list

# Scrape multiple pages
def scrape_jobs(base_url):
    all_jobs = []
    page = 1
    
    while True:
        print(f"Scraping page {page}")
        jobs = scrape_page(base_url + f"&page={page}")
        if not jobs:
            break
        
        all_jobs.extend(jobs)
        page += 1
        time.sleep(2)  # Pause to prevent overwhelming the server
    
    return all_jobs

# Main
if __name__ == "__main__":
    jobs = scrape_jobs(url)
    df = pd.DataFrame(jobs)
    
    # Get the path to the Downloads folder
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    
    # Save the file in the Downloads folder
    df.to_excel(os.path.join(downloads_path, 'upwork_jobs.xlsx'), index=False)
    
    print("Scraping complete. Data saved to 'upwork_jobs.xlsx' in your Downloads folder.")
