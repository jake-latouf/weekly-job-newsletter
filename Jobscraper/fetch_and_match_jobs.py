# jobscraper

import yaml
import requests
import datetime
from bs4 import BeautifulSoup
import smtplib
from email.mim.text import MIMEText


# load user configuration from config.yaml
with open('config.yaml', 'r') as config_file:
    user_config = yaml.safe_load(config_file)

# Set configuration values
email_address = user_config.get('email_address') # required
api_key = user_config.get('api_key') # required
match_criteria = user_config.get('match_criteria', {}) # required
email_day = user_config.get('weekly_email_day', 1) # required

# set configuration values for required nested elements in match_criteria
titles = match_criteria.get('titles', []) # required
years_of_xp = match_criteria.get('years_of_xp', 0) # required
locations = match_criteria.get('locations', []) # required

# initialize two arrays so the required values can be check for null
required_configuration_values = [email_address, api_key, match_criteria, email_day]

# loop through both required values arrays and generate an exception if any of them come up empty
for value in required_configuration_values:
    if not value:
        raise ValueError(f"Missing required value {value}. Please update config.yaml with any required values")

# check if any of the nested elements in match_criteria are empty
if not  titles or years_of_xp is None or not locations: 
    raise ValueError(f"Missing required values in match_criteria. Please update config.yaml with any required values.")

# function to fetch job listings from Indeed
def fetch_job_listings():

    return listings

def match_job_listings(listings):
    return matched_jobs

# export matched jobs to database
