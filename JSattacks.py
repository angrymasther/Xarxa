from scapy.all import *
import os
from scapy.layers import http

def javascriptINJ(pkt):
	print pkt[http]
def sniffer():
	sniff(prn=javascriptINJ, filter="tcp port 80")

sniffer()
