import aiohttp
import asyncio
import time


import aiohttp
import asyncio

async def fetch(session, url):
    async with session.post(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://0.0.0.0:8080/?first=1&second=2')
        print(html)

if __name__ == '__main__':
    start_time = time.time()
    ioloop = asyncio.get_event_loop()
    tasks = [ main() for _ in range(1000)
    ]
    ioloop.run_until_complete(asyncio.wait(tasks))
    ioloop.close()
    print(time.time() - start_time)
