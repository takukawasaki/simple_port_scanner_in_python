#!/usr/bin/python3

import sys
import subprocess
import shlex




try:
    command = 'ping -c 3 localhost'
    args = shlex.split(command)
    res = subprocess.Popen(args,shell=False,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    

    #for line in res.stdout.read():
        
    #     text = line.decode('utf-8')
    #     buf.append(text)
    #     sys.stdout.write(text)

    #     if not line and res.poll() is not None:
    #         break
    f = res.stdout.read().decode().split('\n')
    for line in f:
        print(line)
    res.stdout.close()
    

except KeyboardInterrupt:
    res.kill()

