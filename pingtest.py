#!/usr/bin/python3

import sys
import subprocess
import shlex


try:
    buf =  []
    
    command = 'ping -c 3 localhost'
    args = shlex.split(command)
    res = subprocess.Popen(args,shell=False,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    

    while True:
        line = res.stdout.readline()
        text = line.decode('utf-8')
        buf.append(text)
        sys.stdout.write(text)
        if not line and res.poll() is not None:
            break
    res.stdout.close()
    res.kill()

except KeyboardInterrupt:
    res.kill()

