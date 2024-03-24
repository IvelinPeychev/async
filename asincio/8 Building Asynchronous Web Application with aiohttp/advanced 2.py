import aiohttp
from aiohttp import web
import asyncio
import json

async def handle_get(request):
    # Handler for GET requests
    return web.Response(text="Welcome! This server accepts POST requests at this URL.")

async def handle_post(request):
    # Handler for POST requests with JSON payload
    try:
        data = await request.json()
        # Simulate processing the received data
        response_data = {"received": data, "msg": "Data processed successfully!"}
        return web.json_response(response_data)
    except json.JSONDecodeError:
        return web.Response(status=400, text="Invalid JSON payload")

async def main():
    app = web.Application()
    # Setup routes for GET and POST requests
    app.add_routes([web.get('/', handle_get),
                    web.post('/', handle_post)])

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()

    print("Server started at http://localhost:8080")
    try:
        while True:
            await asyncio.sleep(3600)  # Keep running
    except KeyboardInterrupt:
        pass
    finally:
        await runner.cleanup()

if __name__ == '__main__':
    asyncio.run(main())
