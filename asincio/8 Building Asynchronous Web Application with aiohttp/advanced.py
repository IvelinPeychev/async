import aiohttp
import asyncio
from aiohttp import web


async def hello(req):
    return web.Response(status=201, text='Hello my world')


app = web.Application()
app.add_routes([web.get('/', hello)])

if __name__ == '__main__':
    web.run_app(app, port=3080)

