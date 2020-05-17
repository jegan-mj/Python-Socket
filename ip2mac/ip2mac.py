from scapy.all import *

def ip2mac(ip):
    rsp = srp1(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip), timeout=2, retry=3)
    print(rsp[Ether].src)

ip2mac("192.168.172.1")