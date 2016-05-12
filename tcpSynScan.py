#!/usr/bin/python3

import socket as s
import os
from datetime import datetime

def synScan(addr):
    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    s.setdefaulttimeout(1)
    result = sock.connect_ex((addr, 137))
    if result == 0:
        return 1
    else:
        return 0



net = input("Enter the IP address ")
a = '.'
net1 = net.split(a)
net2 = net1[0] + a + net1[1] + a + net1[2] + a

st1 = int(input("Enter starting number "))
en1 = int(input("Enter end      number "))




def run(start , end):
    print("Start scanning...")
    t1 = datetime.now()
    for ip in range(start , end)    :
        addr = net2 + str(ip)
        if synScan(addr):
            print("{} ------> live".format(addr))
    t2 =datetime.now()
    total = t2 - t1
    print("Scanning completed in {}".format(total))
    
run(st1,en1)    
