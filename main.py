import os
import requests
from bs4 import BeautifulSoup
import schedule
import time



# CONFIGURATION FROM ENVIRONMENT
URL = os.environ.get("URL")
SELECTOR = os.environ.get("SELECTOR")
EXPECTED_TEXT = os.environ.get("EXPECTED_TEXT")
NOTIFY_RUN_CHANNEL = os.environ.get("NOTIFY_RUN_CHANNEL")
INTERVAL_MINUTES = os.environ.get("INTERVAL_MINUTES", "5")  # Default to 5 minutes if not set
NOTIFICATION_TITLE = os.environ.get("NOTIFICATION_TITLE")
NOTIFICATION_TEXT = os.environ.get("NOTIFICATION_TEXT")

# Scrape and check function
def check_page():
    try:
        resp = requests.get(URL, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        element = soup.select_one(SELECTOR)
        if not element:
            print("Selector not found!")
            return
        text = element.get_text(strip=True)
        if text != EXPECTED_TEXT:
            print(f"Change detected! Sending notify.run notification. New text: {text}")
            send_notify_run_notification(text)
        else:
            print("No change detected.")
    except Exception as e:
        print(f"Error: {e}")


# Send notification via notify.run
def send_notify_run_notification(new_text):
    if not NOTIFY_RUN_CHANNEL:
        print("Notify.run channel not set!")
        return
    try:
        msg = NOTIFICATION_TITLE
        if NOTIFICATION_TEXT:
            msg += f"\n\n{NOTIFICATION_TEXT}"
        else:
            msg += f"\n\n{new_text}"
        resp = requests.post(NOTIFY_RUN_CHANNEL, data=msg)
        if resp.status_code == 200:
            print("Notification sent via notify.run.")
        else:
            print(f"Failed to send notify.run notification: {resp.status_code} {resp.text}")
    except Exception as e:
        print(f"Error sending notify.run notification: {e}")

def validate_config():
    """Validate that all required environment variables are set"""
    errors = []
    
    if not URL:
        errors.append("URL environment variable is required")
    
    if not SELECTOR:
        errors.append("SELECTOR environment variable is required")
    
    if not EXPECTED_TEXT:
        errors.append("EXPECTED_TEXT environment variable is required")
    
    if not NOTIFY_RUN_CHANNEL:
        errors.append("NOTIFY_RUN_CHANNEL environment variable is required")
    
    if not INTERVAL_MINUTES:
        errors.append("INTERVAL_MINUTES environment variable is required")
    else:
        try:
            interval = int(INTERVAL_MINUTES)
            if interval <= 0:
                errors.append("INTERVAL_MINUTES must be a positive integer")
        except ValueError:
            errors.append("INTERVAL_MINUTES must be a valid integer")
    
    if not NOTIFICATION_TITLE:
        errors.append("NOTIFICATION_TITLE environment variable is required")
    
    if errors:
        print("Configuration validation failed:")
        for error in errors:
            print(f"  - {error}")
        return False
    
    return True

if __name__ == "__main__":
    print("Starting content change detector...")
    
    # Validate configuration
    if not validate_config():
        print("Exiting due to configuration errors.")
        exit(1)
    
    # Convert INTERVAL_MINUTES to integer after validation
    interval_minutes = int(INTERVAL_MINUTES)
    
    # Schedule the job
    schedule.every(interval_minutes).minutes.do(check_page)
    
    print(f"Configuration valid. Monitoring {URL} every {interval_minutes} minutes...")
    check_page()  # Initial check
    while True:
        schedule.run_pending()
        time.sleep(1)
