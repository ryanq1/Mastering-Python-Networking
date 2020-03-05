from pysnmp.entity.rfc3413.oneliner import cmdgen
cmd_generator = cmdgen.CommandGenerator()


SNMP_HOST = 'localhost'
SNMP_PORT = 161
SNMP_COMMUNITY = 'public'

   error_notify,eorr_status, error_index, var_binds =
   cmd_generator.getCmd(
       cmdgen.CommunityData(SNMP_COMMUNITY),
       cmdgen.UdpTransportTarget((SNMP_HOST, SNMP_PORT))
       cmdgen.MibVaribale('SNMPv2-MIB', 'sysDescr', 0),
       lookupNames=True, lookupValues=True
   )
