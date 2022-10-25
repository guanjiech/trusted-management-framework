import pickle
import time
import logging
import asyncio
import sys

from kademlia.network import Server

if len(sys.argv) != 4:
    print("Usage: python get.py <bootstrap node> <bootstrap port> <key>")
    sys.exit(1)

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log = logging.getLogger('kademlia')
log.addHandler(handler)
log.setLevel(logging.DEBUG)

async def run():
    time1 = time.perf_counter()
    with open("status.json",'rb') as file:
        data = pickle.load(file)
    server = Server(data['ksize'],data['alpha'],data['id'])
    await server.listen(8469)
    if data['neighbors']:
        await server.bootstrap(data['neighbors'])
    time2 = time.perf_counter()
    result = await server.get(sys.argv[3])
    server.stop()
    with open("data_get.txt","a+") as file:
        file.write(str(time.perf_counter()-time1)+","+str(time.perf_counter()-time2)+"\n")
        file.close()
asyncio.run(run())
