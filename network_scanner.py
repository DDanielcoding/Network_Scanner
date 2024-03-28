#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

scan("172.26.160.1/24")