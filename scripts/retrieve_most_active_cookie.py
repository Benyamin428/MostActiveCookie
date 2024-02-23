import argparse
import csv
import logging
import sys
import os

from datetime import datetime

# Validate if input csv file path exists
def file_exists(file_path):
    return os.path.exists(file_path)

# Validates if the input date represents a date in 'YYYY-MM-DD' format
def is_valid_date(date):
    try:
        year, month, day = map(int, date.split('-'))
        datetime(year, month, day)
        return True
    except ValueError:
        return False

# Retrieves the cookie(s) which is the most active based on the provided date
def get_most_active_cookie(csv_file, date):

    # Dictionary to store cookies and their occurrence counts
    cookies = {}

    # Open the CSV file
    with open(csv_file, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            cookie, timestamp = row

            # Extract date portion from the timestamp
            cookie_date = timestamp.split('T')[0]

            # Check if the date matches the specified date
            if cookie_date == date:
                # Increment the cookie's count in the dictionary
                cookies[cookie] = cookies.get(cookie, 0) + 1

    # Calculate the max count of occurrences among the cookies
    max_count = max(cookies.values(), default=0)

    # Find the cookie(s) with the max count
    most_active_cookies = [cookie for cookie, count in cookies.items() if count == max_count]

    print(most_active_cookies)

    return most_active_cookies

if __name__ == "__main__":

    # Logging set-up
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    parser = argparse.ArgumentParser(description='Process some files.')
    parser.add_argument('-f', '--file', required=True, help='Specify the csv file containing the cookies.')
    parser.add_argument('-d', '--date', required=True, help='Specify the date of the cookie you want.')
    args = parser.parse_args()

    csv_file = args.file
    date = args.date

    # Check if file path exists
    if not file_exists(csv_file):
        logging.error("File path does not exist")
        sys.exit(1)

    # Check if input date is valid
    if not is_valid_date(date):
        logging.error("Invalid date format. Please use YYYY-MM-DD.")
        sys.exit(1)

    most_active_cookies = get_most_active_cookie(csv_file, date)

    # Output most active cookie(s) if exists
    if most_active_cookies:
        for cookie in most_active_cookies:
            logging.info(f"Most active cookie(s): {cookie}")
    else:
        logging.info("No cookies found for the specified date.")