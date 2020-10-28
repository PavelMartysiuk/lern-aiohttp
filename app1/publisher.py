import asyncio

from nats.aio.client import Client as NATS


class Publisher:
    def __init__(self, connect,message, notify_subject='events',  loop= asyncio.get_event_loop() ):
        self.nats_server = connect
        self.loop = loop
        self.message = message
        self.notify_subject = notify_subject
        self.nc = NATS()

    async def start(self):
        await self.nc.connect(self.nats_server, loop=self.loop)

    async def send_message(self):
        await self.start()
        await self.nc.publish(self.notify_subject, self.message.encode())
        print('send')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    pub = Publisher(loop=loop, connect="nats://0.0.0.0:4222", message='hello')
    loop.run_until_complete(pub.send_message())
