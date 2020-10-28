import asyncio

from nats.aio.client import Client as NATS
from publisher import Publisher


class Client:
    def __init__(self, connect, loop, notify_subject='events'):
        self.nats_server = connect
        self.loop = loop
        self.notify_subject = notify_subject
        self.nc = NATS()
        self.status = False

    async def events_handler(self, msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        print("Received a message on '{subject} {reply}': {data}".format(
            subject=subject, reply=reply, data=data))
        self.status = True

    async def start(self):
        await  self.nc.connect(self.nats_server, loop=self.loop)
        await self.nc.subscribe(self.notify_subject, cb=self.events_handler)
        print('sub')



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    subscriber = Client(loop=loop, connect='nats://0.0.0.0:4222')
    loop.run_until_complete(subscriber.start())
    loop.run_forever()

