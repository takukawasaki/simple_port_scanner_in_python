#!/usr/bin/python3

import socket as s
import subprocess
import sys
from datetime import datetime


subprocess.run('clear',shell=True)

remote = input("\t Enter the remote ip address: ")
r1 = int(input("\t Enter the start port number: "))
r2 = int (input("\t Enter the end port number: "))

print("\n")
print("*"*40)
print("Scanning start at moment...")
print("*"*40)
print("\n")



t1 = datetime.now()

try:
    for port in range(r1, r2):
        sock = s.socket(s.AF_INET,s.SOCK_STREAM)
        s.setdefaulttimeout(1)

        result = sock.connect_ex((remote, port))
        if result == 0:
            
            print("Port {:<6} ------> open ".format(port))
        sock.close()
except KeyboardInterrupt:
    print("Stop processing...")
    sys.exit()

except s.gaierror:
    print("Host name could not be resolved")
    sys.exit()

except s.error:
    print("Could not connect server ")
    sys.exit()

t2 = datetime.now()

total = t2 - t1
print("Scanning complete in {}".format(total))




