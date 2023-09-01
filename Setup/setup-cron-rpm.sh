#!/bin/bash

if ! rpm -l | grep -q "cron"; then
    echo "cron package is not installed. Installing..."
    dnf update
    dnf -y install cron
    echo "cron package installed successfully"

else
    echo "cron package is already installed."
fi

echo "0 17 * * * /usr/bin/python3 /app/fetch_and_match_jobs.py" > /etc/cron.d/fetch_jobs_cron
echo "0 17 * * 1 /usr/bin/python3 /app/fetch_and_match_jobs.py" > /etc/cron.d/send_listings_cron

chmod 0644 /etc/cron.d/fetch_jobs_cron
chmod 0644 /etc/cron.d/send_listings_cron

cron -f
