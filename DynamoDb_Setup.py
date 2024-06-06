import boto3
import json
#these are the access keys for the access of dynamodb

access_key = "AKIAXYKJR6TKNWPEERAO"
secret_access_key = "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"

session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_access_key,
    region_name='us-east-1'
)

client_dynamo = session.resource('dynamodb')
#search for the table
table = client_dynamo.Table('scrapping') 
records = ""
#this loads the json data into records variable
with open('job_listings.json', 'r') as datafile:  
    records = json.load(datafile)
# print(records('Job title'))
for record in records:
    #Job title is marked as primary for this json dataset. All the job postings are stored in job_title variable
    job_title = record.get('Job title')
    # print(job_title)
    record['Job title'] = job_title 
    #Sending the json data to dynamodb
    response = table.put_item(Item=record)
    # print(record)
