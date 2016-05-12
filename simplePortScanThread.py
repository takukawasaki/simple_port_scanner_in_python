#!/usr/bin/python3

import socket as s
import subprocess
import sys
import threading
import shelve

from datetime import datetime

shelf = shelve.open('scan.db',writeback=True)
shelf['desc'] = {}
data = (shelf['desc'])

def tcpScan(threadname, remoteip,r1, r2, c ):

    try:
        for port in range(r1, r2):
            sock = s.socket(s.AF_INET,s.SOCK_STREAM)
            s.setdefaulttimeout(c)
            result = sock.connect_ex((remoteip, port))
            
            if result == 0:
                
                print("Port open ------> \t {} -- {} ".format(port , data.get(port,"Unknown")))
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

    #shelf.close()



class myThread(threading.Thread):
    def __init__(self,threadName, remoteip, r1, r2,c):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.remoteip = remoteip
        self.r1 = r1
        self.r2 = r2
        self.c = c

    def run(self):
        tcpScan(self.threadName, self.remoteip, self.r1, self.r2, self.c)


d = input("\t press D for domain or press I for ipaddress:\t")

if d == 'D' or d == 'd':
    remoteserver = input("Enter the domain name to scan: ")
    
    scanip = s.gethostbyname(remoteserver)
elif d == 'I' or d == 'i':

    scanip = input("Enter the ip address  to scan:")

else:
    print("Wrong input!!")
    print("Enter D or I")

st = int(input("Enter start port number: "))
en = int(input("Enter end   port number: "))

connect = input("For low connectively press L or high connectively press H\t")

if connect == 'L' or connect == 'l':
    c = 1.5
elif connect == 'H' or connect == 'l':
    c = 0.5
else:
    print("Wrong input.")

    
print("\n")
print("*"*40)
print("Simple port scannnnnnner")
print("*"*40)
print("\n")



t1 = datetime.now()

tp = en - st



#tn : number of ports handled by one thread
tn = 30

#tnum : number of threads
tnum = int(tp/tn)

if tp%tn != 0:
    tnum += 1
    
if tnum > 300:
    tn = tp/300
    tn= tn+1
    tnum=tp/tn
    if tp%tn != 0:
        tnum= tnum+1

threads = []

try:
    for i in range(tnum):
        r2 = en + tn
        thread = myThread("T1",scanip, st, r2, c)
        thread.start()
        threads.append(thread)
        r1_1 = r2


except:
    print("Unable to start thread.")

print("\t Number of Threads active: {}".format(threading.activeCount()))

for t in threads:
    t.join()

print("Exiting main thread.")

shelf.close()
t2 = datetime.now()
total = t2 - t1
print("Scanning complete in {}".format(total))




