import pandas as pd
from influxdb import InfluxDBClient
import os
import time

# Connect to InfluxDB
client = InfluxDBClient(host='localhost', port=8086)

# Switch to the desired database or create it if it doesn't exist
dbname = 'mydb'
if {"name": dbname} not in client.get_list_database():
    client.create_database(dbname)
client.switch_database(dbname)

# Define the directory where the CSV files are located
csv_dir = '/path/to/csv/files'

# Read each CSV file, process the data and store it in the InfluxDB database
while True:
    for file_name in os.listdir(csv_dir):
        if file_name.endswith('.csv'):
            # Load CSV file
            df = pd.read_csv(os.path.join(csv_dir, file_name))

            # Iterate over each row in the DataFrame
            for index, row in df.iterrows():
                station, timestamp, consumption = row[0], row[1], row[2]
                
                # Prepare data
                data = [{
                    "measurement": station,
                    "tags": {
                        "station": station.split('.')[1],
                    },
                    "time": pd.to_datetime(timestamp, unit='s').isoformat(),  # assuming timestamp is in Unix timestamp format
                    "fields": {
                        "consumption": float(consumption)
                    }
                }]
                
                # Write data to InfluxDB
                client.write_points(data)

    time.sleep(300)  # wait for 5 minutes before checking the directory again
