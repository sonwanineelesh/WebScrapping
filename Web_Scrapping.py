import requests
from bs4 import BeautifulSoup
import json
import boto3
from urllib.parse import urljoin

# Function to get soup object
def get_soup(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')

# Function to extract job details
def extract_job_details(job_url):
    
    soup = get_soup(job_url)
    job_details = {
        'Job title': '',
        'Company name': '',
        'Job location': '',
        'Description URL': job_url,
        'Detailed description': '',
        'Company website': '',
        'Company logo URL': '',
        'Company description': '',
        'Company funding information': ''
    }
    #thhis finds the job title of the job
    job_details['Job title'] = soup.find('h1', class_='job_position_title').text.strip() if soup.find('h1', class_='job_position_title') else ''


    #this finds the Location of the job
    job_info_divs = soup.find_all('div', class_='inline-flex items-center')
    for div in job_info_divs:
        div_text = div.get_text()
        if 'Published' not in div_text:
            location = div_text.strip()
            break
    job_details['Job location'] = location if location else ''


    #this finds the name of the company which posted the job
    job_details['Company name'] = soup.find('h2', class_='job_company_title').text.strip() if soup.find('h2', class_='job_company_title') else ''


    #this finds the description of the Job   Some of the description is not available due to premium version of dailyremote
    job_details['Detailed description'] = soup.find('div', class_='job-full-description').text.strip() if soup.find('div', class_='job-full-description') else ''

    #this finds the website of the company which posted the job
    company_website_tag = soup.find('a', class_='job_company_link')
    job_details['Company website'] = urljoin(homepage_url, company_website_tag['href'].strip()) if company_website_tag else ''

    #this finds the logo of the company which posted the job
    company_logo_tag = soup.find('img', class_='job_company_logo')
    job_details['Company logo URL'] = urljoin(homepage_url, company_logo_tag['src'].strip()) if company_logo_tag else ''

    #this finds the description of the company which posted the job. Some of the description is not available due to premium version of dailyremote
    job_details['Company description'] = "Company Description is not available because of premium version of dailyremote"

    #Information is not available due to premium version of dailyremote
    job_details['Company funding information'] = "Company Description is not available because of premium version of dailyremote"

    return job_details

# Function to scrape jobs from the homepage
def scrape_jobs(homepage_url):
    soup = get_soup(homepage_url)
    #this finds all divs containing job listing
    job_listings = soup.find_all('div', class_='info-container')
    # print(job_listings)
    for job_listing in job_listings:
        # print("neelesh")
        
        job_url_tag = job_listing.find('div', class_='profile-information')
        job_url_tag1 = job_url_tag.find('h2', class_ = 'job-position')
        job_url = job_url_tag1.find('a')['href']
        #joining the two urls
        url = urljoin(homepage_url, job_url)
        # print(job_url['href'])
        # print(url)
        
        job_details = extract_job_details(url)
        jobs.append(job_details)
    
    return jobs

homepage_url = 'https://dailyremote.com/'
jobs = []
try:
    jobs = scrape_jobs(homepage_url)
    print(json.dumps(jobs, indent=4))
    #Saving the jobs into the json file
    with open('job_listings.json', 'w') as file:
        json.dump(jobs, file, indent=4)
except requests.exceptions.RequestException as e:
    print(f"Failed to retrieve jobs from homepage: {e}")
