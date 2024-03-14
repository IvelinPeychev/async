import aiohttp
import asyncio

urls = ['http://example.com', 'https://www.python.org', 'https://httpbin.org/get']

async def foo(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response_text = await response.text()
            print(f"Async request completed with response length: {len(response_text)}")


async def main():
    print("Starting asynchronous request")
    await asyncio.gather(*(foo(url) for url in urls))


if __name__ == '__main__':
    asyncio.run(main())

