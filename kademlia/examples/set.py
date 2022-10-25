import logging
import asyncio
import sys
import time
import os
import pickle

from kademlia.network import Server

if len(sys.argv) != 5:
    print("Usage: python set.py <bootstrap node> <bootstrap port> <key> <value>")
    sys.exit(1)

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log = logging.getLogger('kademlia')
log.addHandler(handler)
log.setLevel(logging.DEBUG)

async def run():
    time2 = time.perf_counter()
    if not os.path.exists("status.json"):
        server = Server()
        await server.listen(8469)
        bootstrap_node = (sys.argv[1], int(sys.argv[2]))
        await server.bootstrap([bootstrap_node])
    else:
        with open("status.json",'rb') as file:
            data = pickle.load(file)
        server = Server(data['ksize'],data['alpha'],data['id'])
        await server.listen(8469)
        if data['neighbors']:
            await server.bootstrap(data['neighbors'])
    time1 = time.perf_counter()
    f = open(sys.argv[4],encoding="utf-8")
    await server.set(sys.argv[3], f.read())
    server.save_state("status.json")
    server.stop()
    with open("data.txt","a+") as file:
        file.write(str(time.perf_counter()-time2)+","+str(time.perf_counter()-time1)+"\n")
        file.close()
    print(time.perf_counter()-time2)
    print(time.perf_counter()-time1)
asyncio.run(run())
