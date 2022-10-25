from concurrent.futures import ThreadPoolExecutor
import threading
import time
import os

def action(port):
    os.system("nohup python3 node.py -p %s >> %sout.log 2>&1 &" % (port,port))
pool = ThreadPoolExecutor(max_workers=50)

for port in range(1,50):
    future = pool.submit(action,8000+port)
time.sleep(300)
pool.shutdown()
