from influxdb import InfluxDBClient

client = InfluxDBClient(host="10.89.188.28", port="8086")


def create_db(db_name):
    # Creates the database in InfluxDB if it does not exist
    dbs = client.get_list_database()
    db_names = [db["name"] for db in dbs]
    if db_name not in db_names:
        print("Creating '{}' in InfluxDB".format(db_name))
        client.create_database(db_name)
    else:
        print("Database '{}' in InfluxDB already".format(db_name))


if __name__ == "__main__":
    db_name = "snmp"
    create_db(db_name)
    client.switch_database(db_name)
