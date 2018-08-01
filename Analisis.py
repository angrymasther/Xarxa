# -*- coding: utf-8 -*-
import os
import socket
from scapy.all import *

def PingScan(IPExample): #-pM --PingMap
    IPBoceto = IPExample[:-1]
    IPs = []
    for x in range(255):
        ip = IPBoceto + str(x)
        ping = os.system("ping -c 1 " + ip)
        if ping == 0:
            IPs.append(ip)
    for x in IPs:
        print x
    return IPs

def ArpScan(IPExample): #-aM --ArpMap
    IPBoceto = IPExample[:-1]
    IPs = []
    for x in range(255):
        ip = IPBoceto + str(x)
        paquete = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=1,pdst=ip)
        resp, unans = srp(paquete, timeout=10, verbose=False)
        for s,r in resp:

            if r[Ether].src > 0:
                print ip
                IPs.append(ip)
        return IPs

def SockScan(IP): # -sTS --SockTCPScan
    ports = []
    for x in range(65535):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            conexion = s.connect_ex((IP,x))
            if conexion == 0:
                service = s.recv(1024)
                print service
                print "Puerto "+str(x)+" abierto"+" "+service
                ports.append(str(x))
            s.close()
        except socket.timeout:
            print "Puerto "+str(x)+" abierto"

    return ports

def SockUDPScan(IP): #sUS --SockUDPScan
    ports = []
    for x in range(65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        conexion = s.connect_ex((IP,x))
        if conexion == 0:
            print "Puerto "+str(x)+" abierto"
            ports.append(str(x))
        s.close()
    return ports

def halfSynScan(ip): #hsS
    ports = []
    for x in range(65535):
        ipp = IP(dst=ip)
        syn = TCP(dport=x, flags="S")
        send = sr1(ipp/syn, timeout=10, verbose=False)
        try:
            if send[1].flags == "SA":
                rst = TCP(dport=x, flags="R")
                sr1(ipp/rst , timeout=10, verbose=False)
                ports.append(x)
                print "Puerto "+str(x)+" abierto"
        except TypeError:
            pass

def finScan(ip, time): #fS
    print """
    [!] ADVERTENCIA: este escaneo es poco preciso por lo que algunos resultados pueden ser incorrectos.
    Si necesitas mas precisión prueba a aumentar el timeout (por defecto 10)

    [!] ADVERTENCIA: Este escaneo no funciona en los siguientes equipos: Windows , Cisco , HP-UX , IRIX.
    Esto pasa porque estos equipos no siguen el estándar RFC 793 y envían un paquete RST cuando el puerto está abierto.
    Esto nos resultaría en todos los puertos cerrados."""

    ports = []
    for x in range(65535):
        ipp = IP(dst=ip)
        fin = TCP(dport=x, flags="F")
        send = sr1(ipp/fin , timeout=time, verbose=False)
        if send == None:
            ports.append(x)
            print "Puerto "+str(x)+" abierto"
    return ports
