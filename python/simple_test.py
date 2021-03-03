from pysnmp.hlapi import *
import sys

COMMUNITY = "read"
HOST = "10.90.148.205"
MIB = "DOCS-RPHY-MIB"
OID = "docsRphyRpdIfEnetPhysAddress"
ENDPOINT = 0


def walk(host, oid):
    for (errorIndication,
         errorStatus,
         errorIndex,
         varBinds) in nextCmd(SnmpEngine(),
                              CommunityData(COMMUNITY),
                              UdpTransportTarget((host, 161)),
                              ContextData(),
                              ObjectType(ObjectIdentity(oid)),
                              lexicographicMode=False):
        if errorIndication:
            print(errorIndication, file=sys.stderr)
            break
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'), file=sys.stderr)
            break
        else:
            for varBind in varBinds:
                print(varBind)


walk(HOST, '.1.3.6.1.4.1.4491.2.1.30.1.2.3.1.7')  # MAC address of RPD
walk(HOST, '.1.3.6.1.4.1.4491.2.1.30.1.2.8.1.31')  # TX Power of SFP
walk(HOST, '.1.3.6.1.4.1.4491.2.1.30.1.2.8.1.32')  # RX Power of SFP

