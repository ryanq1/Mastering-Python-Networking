import socket
import netifaces

if __name__ == '__main__':
	host_name = socket.gethostname()
	ip_address = socket.gethostbyname(host_name)
	print("Host name: {0}".format(host_name))

	ifaces = netifaces.interfaces()
	for iface in ifaces:
		ipaddrs = netifaces.ifaddresses(iface)
		if netifaces.AF_INET in ipaddrs:
			ipaddr_desc = ipaddrs[netifaces.AF_INET]
			ipaddr_desc = ipaddr_desc[0]
			print("Network interface : {0}".format(iface))
			print("\tIP address: {0}".format(ipaddr_desc['addr']))
			print("\tNetmask: {0}".format(ipaddr_desc['netmask']))

	gateways = netifaces.gateways()
	print("Default gateway:\
	{0}".format(gateways['default'][netifaces.AF_INET][0]))
