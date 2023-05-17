import requests
import pandas as pd
import pandas as pd

def download_time_series_data(indicator_code, country_code):
    base_url = "https://api.worldbank.org/v2"
    url = f"{base_url}/country/{country_code}/indicator/{indicator_code}?format=json"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to download data. Status code: {response.status_code}")
        return None
    

def convert_to_dataframe(data):
    series_data = data[1]  # Access the series data from the response

    # Extract relevant information from each dictionary in the series data
    processed_data = [
        {
            'date': entry['date'],
            'value': entry['value']
        }
        for entry in series_data
    ]

    # Create a Pandas DataFrame from the processed data
    df = pd.DataFrame(processed_data)

    # Convert the 'date' column to datetime format
    df['date'] = pd.to_datetime(df['date'])

    # Set the 'date' column as the index
    df.set_index('date', inplace=True)

    # Sort the DataFrame by the index (date)
    df.sort_index(inplace=True)

    return df