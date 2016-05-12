#!/usr/bin/python3

import os
import platform
from datetime import datetime
import subprocess
import shlex


net = input("Enter the network address ")
net1 = net.split('.')

a = '.'
net2 = net1[0] + a + net1[1] + a + net1[2] + a 

st1 = int(input("Enter the starting number "))
en1 = int(input("Enter the last number "))

en1 += 1


oper = platform.system()

if oper == 'Windows':
    ping1 = "ping -n 1 "
elif oper == "Linux" :
    ping1 = "ping -c 1 "

else:
    ping1 = "ping -c 1 "    
    
    

t1 = datetime.now()

print("Scanning in progress...")

try:
    for port in range(st1, en1):
        addr = net2 + str(port)
        command = ping1 + addr
        args = shlex.split(command)
        response = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        f = response.stdout.read().decode().split('\n')
        for line in f:
            #print(line)
            if  not line.count("ttl"):
                continue

            if line.count("ttl"):
                 print("{} ------> live".format(addr))
                
        response.kill()
            
except:
    response.kill()

        
t2 = datetime.now()
total = t2 - t1
print("Scanning complete in {}".format(total))            
            
            
    
        
    
    

