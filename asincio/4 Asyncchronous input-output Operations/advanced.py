import asyncio
import aiohttp

urls = ['https://test.com', 'https://test.com/', 'https://test.com']

async def foo(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(await response.text())



async def foo2(items):
    tasks = []
    for url in items:
        task = asyncio.create_task(foo(url))
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(foo2(urls))
