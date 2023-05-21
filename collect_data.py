import os
import time

import pandas as pd

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

from dotenv import load_dotenv

load_dotenv()  # Loading the environment variables

# Create an InfluxDB Client instance
client = InfluxDBClient(
    url="http://localhost:8086", 
    token=os.getenv('INFLUXDB_TOKEN'), 
    org=os.getenv('INFLUXDB_ORG')
)

# Create a write API instance
write_api = client.write_api(write_options=SYNCHRONOUS)

# Read each CSV file, process the data and store it in the InfluxDB database
while True:
    print("Checking for new data...")
    for file_name in os.listdir('data'):
        print(f"Processing {file_name}...")
        if file_name.endswith('.csv'):
            # Load CSV file
            df = pd.read_csv(os.path.join('data', file_name))

            # Iterate over each row in the DataFrame
            for index, row in df.iterrows():
                station, timestamp, consumption = row[0], row[1], row[2]
                print(f"Storing data for {station}...")

                # Create a data point
                point = (
                    Point(station)
                    .tag("station", station.split('.')[1])
                    .time(pd.to_datetime(timestamp, unit='s').isoformat(), WritePrecision.NS)
                    .field("consumption", float(consumption))
                )
                
                # Write data to InfluxDB
                write_api.write(bucket=os.getenv("INFLUXDB_BUCKET"), org=os.getenv("INFLUXDB_ORG"), record=point)

                # separate points by 1 second
                time.sleep(1) 

                print(f"Data for {station} stored successfully!")
                
                # Delete the CSV file
                os.remove(os.path.join('data', file_name))

    print("Job done!")
    time.sleep(300)  # wait for 5 minutes before checking the directory again
