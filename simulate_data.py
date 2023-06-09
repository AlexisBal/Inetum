import csv
import random
import time
from datetime import datetime

# List of stations
stations = ["Station1", "Station2", "Station3", "Station4", "Station5", "Station6", "Station7"]

# Function to generate consumption data
def generate_data():
    data = []
    for station in stations:
        print(f"Generating data for {station}...")
        elec_kwh = round(random.uniform(50, 100), 2)  # electricity consumption in KWh
        fluid_lh = round(random.uniform(10, 30), 2)  # fluid consumption in L/h
        data.append([f'PLCNext-{station}.Conso_Kwh', int(time.mktime(datetime.now().timetuple())), elec_kwh])
        data.append([f'PLCNext-{station}.Conso_Lh', int(time.mktime(datetime.now().timetuple())), fluid_lh])
        print(f"Data generated for {station} successfully!")
    return data

# Function to write data to CSV file
def write_to_csv(data):
    print("Writing data to CSV file...")
    filename = f'data/{int(time.mktime(datetime.now().timetuple()))}_conso_ts.csv'
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
        file.close()
    print("Data written to CSV file successfully!")

# Generate and write data every 5 minutes
while True:
    print("Generating data...")
    data = generate_data()
    write_to_csv(data)
    print("Data generated successfully!")
    time.sleep(10)  # sleep for 5 minutes
