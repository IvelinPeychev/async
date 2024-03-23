import asyncio

async def async_counter(to):
    for i in range(to):
        yield i
        await asyncio.sleep(1)

async def consume():
    async for number in async_counter(3):
        print(f"Received {number}")

asyncio.run(consume())

