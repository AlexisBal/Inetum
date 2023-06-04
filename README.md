# Inetum: Energy Consumption Monitoring

This project allows for the monitoring of electrical and fluid consumption in a set of stations. The project is structured into two main parts:

1. **Data generation and collection**: This is done using a Python script which periodically generates CSV files simulating the consumption data for each station.

2. **Data visualization**: The generated data is visualized using Grafana, which reads from an InfluxDB instance where the data is stored.

## Prerequisites

To run this project, you need to have the following installed:

- Python 3.x
- InfluxDB 2.x
- Grafana 7.x

You also need the Python libraries specified in `requirements.txt`. You can install them using pip:

```
pip install -r requirements.txt
```

## Usage

### Data Generation

You can generate data using the `generate_data.py` script. The script generates electricity and fluid consumption data for a list of stations. Each entry is timestamped and written to a CSV file.

To run the script:

```bash
python generate_data.py
```

### Data Collection

The `collect_data.py` script reads the generated CSV files and writes the data to an InfluxDB database.

First, you need to set the environment variables in a `.env` file:

```
INFLUXDB_TOKEN=your_influxdb_token
INFLUXDB_ORG=your_influxdb_organization
INFLUXDB_BUCKET=your_influxdb_bucket
```

To run the script:

```bash
python collect_data.py
```

### Data Visualization

The data can be visualized in Grafana. To do this, connect Grafana to your InfluxDB data source and create a new dashboard. You can use Flux queries to fetch and aggregate data from InfluxDB.

Refer to the [Grafana documentation](https://grafana.com/docs/grafana/latest/) for detailed instructions on how to create and configure dashboards.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

---

**Note:** This project is for demonstration purposes only and does not represent a real-world application. The generated data is random and does not reflect actual consumption patterns.
