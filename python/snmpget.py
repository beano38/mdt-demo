import os
import sys

# PyPI Libraries
from pysnmp.hlapi import *
import oyaml as yaml

# Local python files
from database_insert import create_measurement

CONFIG_FILE = os.getenv("config", "config.yml")

# Load the Config File
try:
    with open(CONFIG_FILE) as f:
        config = yaml.safe_load(f)
except FileNotFoundError:
    print("CRITICAL:  Configuration file not found, devault falue is 'config.yml'")
    sys.exit(1)

# List of returned snmp data
output = []


def snmp_get(host, community, port, oid, device_type):
    global output
    errorIndication, errorStatus, errorIndex, varBinds = next(getCmd(SnmpEngine(),
                                                                     CommunityData(community),
                                                                     UdpTransportTarget((host, port)),
                                                                     ContextData(),
                                                                     ObjectType(ObjectIdentity(oid["mib"], oid["oid"], oid["endpoint"]))
                                                                     )
                                                              )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            # Format the response from snmpget
            mib_output = ' = '.join([x.prettyPrint() for x in varBind]).split(" = ")
            mib_output = mib_output[1]

            # Set the data in the format that InfluxDB expects
            output.append({
                "measurement": "{}-{}".format(device_type.upper(), oid["mib"]),
                "tags": {
                    "source": host
                },
                "fields": {
                    "{}.{}".format(oid["oid"], oid["endpoint"]): mib_output,
                }
            })

    return output


def gather_data(host, device_type):
    global output
    if device_type == 'cmts':
        for oid in config["cmts"]["oids"]:
            snmp_get(host, config["cmts"]["community_string"], config["cmts"]["port"], oid, device_type)
    elif device_type == 'cm':
        for oid in config["cm"]["oids"]:
            snmp_get(host, config["cm"]["community_string"], config["cm"]["port"], oid, device_type)

    if output:
        create_measurement(db_name=config["influxdb"]["snmp_db"], measurement=output)

    return output


if __name__ == "__main__":
    cbr8 = "10.90.148.205"
    output = gather_data(host=cbr8, device_type="cmts")
    import json
    print(json.dumps(output, indent=2))

