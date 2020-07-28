import os
import sys

# PyPI Libraries
from pysnmp.hlapi.asyncore import *
import oyaml as yaml

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


def cbFun(snmpEngine, sendRequestHandle, errorIndication, errorStatus, errorIndex, varBinds, cbCtx):
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        output.append(varBinds)
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))


def snmp_get(host, community, port, oid):
    engine = SnmpEngine()
    getCmd(
        engine,
        CommunityData(community),
        UdpTransportTarget((host, port)),
        ContextData(),
        ObjectType(ObjectIdentity(oid["mib"], oid["oid"], oid["endpoint"])),
        cbFun=cbFun
    )
    engine.transportDispatcher.runDispatcher()


def gather_data(host, device_type):
    global output
    if device_type == 'cmts':
        for oid in config["cmts"]["oids"]:
            snmp_get(host, config["cmts"]["community_string"], config["cmts"]["port"], oid)
    elif device_type == 'cm':
        for oid in config["cm"]["oids"]:
            snmp_get(host, config["cm"]["community_string"], config["cm"]["port"], oid)
    return output


if __name__ == "__main__":
    cbr8 = "10.90.148.205"
    output = gather_data(host=cbr8, device_type="cmts")

