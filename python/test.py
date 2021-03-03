from pysnmp.hlapi import *
import os

local_mibs = "/Users/beelder/.snmp/mibs"
remote_mibs = 'http://mibs.snmplabs.com/asn1/@mib@'

for (errorIndication,
     errorStatus,
     errorIndex,
     varBinds) in nextCmd(SnmpEngine(),
                          CommunityData('read', mpModel=0),
                          UdpTransportTarget(("10.90.148.205", 161)),
                          ContextData(),
                          ObjectType(ObjectIdentity('DOCS-RPHY-MIB', 'docsRphyRpdDevIdSerialNum').addAsn1MibSource(remote_mibs)),
                          # ObjectType(ObjectIdentity('DOCS-IF-MIB', 'docsIfCmtsCmStatusMacAddress').addAsn1MibSource(remote_mibs)),
                          # ObjectType(ObjectIdentity('DOCS-IF-MIB', 'docsIfCmtsCmStatusIpAddress').addAsn1MibSource(remote_mibs)),
                          # ObjectType(ObjectIdentity('DOCS-IF-MIB', 'cmtsCmRegStatusMdCmSgId').addAsn1MibSource(remote_mibs)),
                          # ObjectType(ObjectIdentity('DOCS-RPHY-MIB', 'docsRphyRpdIfEnetSfpPlusStatusMeasuredRxInputPwr').addAsn1MibSource(local_mibs)),
                          # ObjectType(ObjectIdentity('DOCS-RPHY-MIB', 'ifPhysAddress')),
                          # ObjectType(ObjectIdentity('DOCS-RPHY-MIB', 'ifType')),
                          lexicographicMode=False):

    if errorIndication:
        print("error here")
        print(errorIndication)
        break
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex)-1][0] or '?'))
        break
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))