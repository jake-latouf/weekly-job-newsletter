# Send matched jobs
# retrieve matched jobs from storage

if not matched_jobs:
    return

email_body = "Hello from jobscraper! Here are your matching jobs for this week: \n\n"
for job in matched_jobs:
    email_body += f"- {job['jobtitle']} ({job['location']})\n"
    email_body += f" {job['url']}\n\n"

# create message
msg = MIMEText(email_body)
msg['Subject'] = 'Weekly Job Matches'
msg['From'] = 'Job.Bot@jobscraper.com'
msg['To'] = email_address