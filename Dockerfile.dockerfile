FROM python:3.8

WORKDIR /weekly-job-newsletter

#Install python library dependencies
RUN pip install requests bs4

# copy setup scripts and app source code into container
COPY Setup/ /weekly-job-newsletter/Setup/
COPY Jobscraper/ /weekly-job-newsletter/Jobscraper/ 

# Make both setup scripts executable
RUN chmod +x /weekly-job-newsletter/Setup/setup-cron-deb.sh
RUN chmod +x /weekly-job-newsletter/Setup/setup-cron-rpm.sh
RUN chmod +x /weekly-job-newsletter/Setup/setup.py

#Run setup scripts and then run app
CMD ["/bin/bash", "-c", "/usr/bin/python3 /weekly-job-newsletter/Setup/setup.py"]