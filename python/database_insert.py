import os
import sys

# PyPI Libraries
from influxdb import InfluxDBClient
import oyaml as yaml

CONFIG_FILE = os.getenv("config", "config.yml")

# Load the Config File
try:
    with open(CONFIG_FILE) as f:
        config = yaml.safe_load(f)
except FileNotFoundError:
    print("CRITICAL:  Configuration file not found, default value is 'config.yml'")
    sys.exit(1)


client = InfluxDBClient(host=config["influxdb"]["host"], port=config["influxdb"]["port"])


def create_db(db_name):
    # Creates the database in InfluxDB if it does not exist
    dbs = client.get_list_database()
    db_names = [db["name"] for db in dbs]
    if db_name not in db_names:
        print("Creating '{}' in InfluxDB".format(db_name))
        client.create_database(db_name)
        return True
    else:
        print("Database '{}' in InfluxDB already".format(db_name))
        return False


def create_measurement(db_name, measurement):
    client.write_points(measurement, database=db_name)


if config["influxdb"]["create_db"] == "True":
    create_db(config["influxdb"]["snmp_db"])

json_body = [
        {
            "measurement": "cpu_load_short",
            "tags": {
                "host": "server01",
                "region": "us-west"
            },
            "time": "2009-11-10T23:01:00Z",
            "fields": {
                "Float_value": 0.64,
                "Int_value": 5,
                "String_value": "Text",
                "Bool_value": True
            }
        }
    ]

if __name__ == "__main__":
    db_name = "snmp"
    # create_db(db_name)
    create_measurement(db_name, measurement=json_body)
