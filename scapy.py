from scapy.all import *

pkt = IP(src="192.168.0.1", dst="8.8.8.8")/TCP(sport=1234, dport=80)

send(pkt)
