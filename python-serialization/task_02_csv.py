#!/usr/bin/env python3
"""This module read data from a CSV and convert it to JSON"""

import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file and converts it into a JSON file.

    Args:
        csv_filename (str): The path to the source CSV file.

    Returns:
        bool: True if successful, False if an error occurred.
    """
    try:
        # 1. Open the CSV file for reading
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            # 2. Use DictReader to turn rows into dictionaries automatically
            csv_reader = csv.DictReader(csv_file)
            
            # Convert the reader object into a list of dictionaries
            data_list = [row for row in csv_reader]

        # 3. Serialize the list and write to data.json
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            # indent=4 makes the resulting JSON human-readable
            json.dump(data_list, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: The file '{csv_filename}' was not found.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
