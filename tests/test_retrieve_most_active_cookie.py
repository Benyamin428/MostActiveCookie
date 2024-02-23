import pytest
import csv
from scripts.retrieve_most_active_cookie import get_most_active_cookie, is_valid_date, file_exists
import tempfile
import os

@pytest.fixture
def test_csv_file():
    csv_file = os.path.join(os.path.dirname(__file__), 'test_cookie_log.csv')
    return csv_file

def test_file_exists():
    assert file_exists('bad_file_path.csv') == False
    assert file_exists(__file__) == True

def test_is_valid_date():
    assert is_valid_date('2024-02-22') == True
    assert is_valid_date('2024-02-30') == False
    assert is_valid_date('2024-13-01') == False

def test_get_most_active_cookie(test_csv_file):
    date = '2018-12-09'
    expected_most_active_cookies = ['AtY0laUfhglK3lC7']
    assert get_most_active_cookie(test_csv_file, date) == expected_most_active_cookies

    date = '2018-12-08'
    expected_most_active_cookies = ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG']
    assert get_most_active_cookie(test_csv_file, date) == expected_most_active_cookies

    date = '2018-12-07'
    expected_most_active_cookies = ['4sMM2LxV07bPJzwf']
    assert get_most_active_cookie(test_csv_file, date) == expected_most_active_cookies

    date = '2018-12-10'  # Date that doesn't exist in CSV
    assert get_most_active_cookie(test_csv_file, date) == []
