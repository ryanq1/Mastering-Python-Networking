#!/usr/bin/env python2

from scapy.all import *

def icmp_ping(destination):
	ans, unans = sr(IP(dst=destination)/ICMP())
	return ans

def tcp_ping(destination, dport):
	ans, uans = sr(IP(dst=destination)/TCP(dport=dport, flags= "S"))
	return ans

def udp_ping(destination):
	ans, unans = sr(IP(dst=destination)/UDP(dport=0))
	return ans

def answer_summary(answer_list):
	answer_list.summary(lambda(s, r): r.sprintf("%IP.src% is alive"))

def main():
	print("** ICMP Ping **")
	ans = icmp_ping("192.168.42.245")
	answer_summary(ans)
	print("TCp ping")
	ans = tcp_ping("192.168.42.245", 22)
	answer_summary(ans)
	print("UDP ping")
	ans = udp_ping("192.168.42.245")
	answer_summary(ans)


if __name__ == "__main__":
	main()
