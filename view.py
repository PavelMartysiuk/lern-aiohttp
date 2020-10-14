from aiohttp import web
import json
import asyncio
import random


async def calculate(request):
    response_obj = {'result': int(request.query['first']) + int(request.query['second']), 'status': 'success'}
    await asyncio.sleep(random.randint(0, 5))
    return web.Response(text=json.dumps(response_obj), status=200)



