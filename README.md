# Most Active Cookie 

## Overview:
This is a command-line program to identify the most active cookie(s) on a specific date.

## Prerequisites:
    - Python installed on your system.

## Setup Virtual Environment:
    It's recommended to set up a virtual environment to manage dependencies.

    For Windows:
    1. Open Command Prompt and navigate to your project directory.
    2. Run:
        python -m venv venv
        venv\Scripts\activate
    
    For Linux:
    1. Open Terminal and navigate to your project directory.
    2. Run:
        python3 -m venv venv
        source venv/bin/activate

## Install Required Packages:
    Once the virtual environment is set up, you can install the required packages using the provided 'requirements.txt' file.
    1. Ensure your virtual environment is activated.
    2. Run the following command to install the required packages:
        
        pip install -r requirements.txt
    
This command will install all the dependencies specified in the 'requirements.txt' file.

## How to use:
As part of the command-line program, there are two parameters that are accepted:
-f: Path to the csv file.
-d: Date in the format YYYY-MM-DD.
    
    Example:
    $ python scripts/retrieve_most_active_cookie.py  -f data/cookie_log.csv -d 2018-12-09
This will output the most active cookie(s) for the specified date.

## Functions:
    
    - get_most_active_cookie(csv_file, date):
        Retrieve the most active cookie(s) based on the provided date from the given CSV file.
    
    - is_valid_date(date):
        Validate if the input date represents a valid date in the format 'YYYY-MM-DD'.

    - file_exists(file_path):
        Validate if the input file path exists.

## Running Tests:
Unit test have been written using pytest. 
To run the unit tests, navigate to the root directory of the project in your terminal and execute the following command:
    
    python -m pytest tests/test_retrieve_most_active_cookie.py
