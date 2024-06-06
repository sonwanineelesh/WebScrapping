
                                                  Web Scrapping of https://dailyremote.com/

This project scrapes job listings from the [DailyRemote](https://dailyremote.com/) website and uploads the extracted data to an AWS DynamoDB table. The job details are first saved into a JSON file and then uploaded to the DynamoDB table named `scrapping`.


Features

Scrapes job titles, company names, job locations, detailed descriptions, company websites, and company logos from DailyRemote.
- Saves the scraped data into a JSON file.
- Uploads the job data from the JSON file to an AWS DynamoDB table.

Dependencies

requests: To make HTTP requests to the website.
beautifulsoup4: To parse HTML and extract job details.
boto3: For interacting with AWS services (not used in the current script but imported).
urllib3: To handle URL operations.

You can install these dependencies using:
pip install requests beautifulsoup4 boto3 urllib3


The DynamoDB table should have the following schema:
Table Name: scrapping
Primary Key: Job title (String)

To run the project you just need to run the files only nothing else you have to do.
_____________________________________________________________________________________________________________________________________________________________________________________________________________

Note - I know access key is the sensitive thing but dynamodb can't be opened without access keys so I have mentioned in the code itself.


