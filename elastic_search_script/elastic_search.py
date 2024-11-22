#!/usr/bin/python3

import requests
from requests.auth import HTTPBasicAuth
import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Suppress InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Configuration
ELASTICSEARCH_URL = "https://localhost"
USERNAME = ""
PASSWORD = ""

indices = []


def get_indices(start_date, end_date):
    response = requests.get(
                f"{ELASTICSEARCH_URL}/_cat/indices?v",
                auth=HTTPBasicAuth(USERNAME, PASSWORD),
                verify=False
    )
    if response.status_code == 200:
        lines = response.text.splitlines()
        for line in lines:

            # Check if the line contains enough parts and the expected format
            parts = line.split()
            if len(parts) > 2:
                index_name = parts[2]  # Extract the index name
                # Check if the index name matches the expected pattern
                if "ds-filebeat-8.6.2-" in index_name:
                    index_date_str = index_name.split('-')[3]  # Extract the date part "YYYY.MM.DD"
                    try:
                        # Convert to datetime object to compare
                        index_date = datetime.datetime.strptime(index_date_str, "%Y.%m.%d")

                        # Convert start_date to datetime for comparison
                        start_date_datetime = datetime.datetime.combine(start_date, datetime.datetime.min.time())

                        if index_date < start_date_datetime:  # Only include indices older than start_date
                            indices.append(index_name)
                    except ValueError:
                        # Skip lines with invalid date formats
                        print(f"Skipping invalid date: {index_date_str}")
                        continue
            else:
                print(f"Skipping invalid line format: {line}")

    else:
        print(f"Failed to retrieve indices: {response.status_code}")
    return indices


def delete_indices(indices):
    for index in indices:
        response_delete = requests.delete(
            f"{ELASTICSEARCH_URL}/{index}",
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            verify=False
        )
        if response_delete.status_code in (200, 204):
            print(f"Deleted index: {index}")
        else:
            print(f"Failed to delete index {index}: {response_delete.status_code}")


if __name__ == "__main__":

    # Calculate today's date and the date 30 days ago
    today = datetime.date.today()
    delta = datetime.timedelta(days=30)
    past_date = today - delta

    # Format the dates as YYYY.MM.DD
    start_date = past_date
    end_date = today

    print(f"Deleting indices older than: {start_date}")

    # Get the indices within the date range
    indices_to_delete = get_indices(start_date, end_date)
    if indices_to_delete:
        print(f"Found indices to delete for {start_date} to {end_date}:")
        for index in indices_to_delete:
            print(index)

        # Automatically delete the indices without confirmation
        delete_indices(indices_to_delete)
        print("Deletion completed.")
    else:
        print(f"No indices found for the specified date range {start_date} -> {end_date}.")