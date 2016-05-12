###!/usr/bin/python3

import os
import subprocess
import shlex
from datetime import datetime
import platform
import socket
import threading
import collections




dic = collections.OrderedDict()

net = input("Enter the IP address ")
a = '.'
net1 = net.split(a)
net2 = net1[0] + a + net1[1] + a + net1[2] + a

st1 = int(input("Enter starting number "))
en1 = int(input("Enter end      number "))


oper = platform.system()

if oper == 'Windows':
    ping1 = "ping -n 1 "
elif oper == "Linux" :
    ping1 = "ping -c 1 "

else:
    ping1 = "ping -c 1 "    
    

t1 = datetime.now()


def run1(st1, en1):
    try:
        for ip in range(st1, en1):
            addr = net2 + str(ip)
            command = ping1 + addr
            args = shlex.split(command)
            response = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            f = response.stdout.read().decode().split('\n')
            for line in f:
                if  not line.count("ttl"):
                    continue

                if line.count("ttl"):

                    dic[ip]  = addr 
            response.kill()
    except:
        response.kill()

        
class myThread(threading.Thread):
    def __init__(self,st,en):
        threading.Thread.__init__(self)
        self.st = st
        self.en = en
    def run(self):
        run1(self.st, self.en)
    

total_ip = en1 - st1
threadN = 20

totalThread = int(total_ip / threadN)
totalThread += 1

threads = []

try:
    for i in range(totalThread):
        en = st1 + threadN
        if en > en1:
            en = en1
        thread = myThread(st1, en)
        thread.start()
        threads.append(thread)
        st1 = en
        
except Error as e:
    print("Error: unable to starting thread {}".format(e))

    
    
print("\tNumber of threads active: {}".format(threading.activeCount()))

for t in threads:
    t.join()

print("exit main threads")
dict = collections.OrderedDict(sorted(dic.items()))

for key in dict:
    print("{:<15} ------> live ".format(dict[key]))

t2 = datetime.now()
total = t2 - t1
print("Scanning complete in {}".format(total))

        
