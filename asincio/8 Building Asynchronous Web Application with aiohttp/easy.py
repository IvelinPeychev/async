import asyncio
import aiohttp
import aiofiles


async def scraper(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def write(url):
    content = await scraper(url)
    with aiofiles(f'{url}.txt', 'w') as file:
        file.write(content)


async def main(urls: list):
    tasks = [asyncio.create_task(write(url)) for url in urls]

    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main(['https://example.com', 'https://example2.com', 'https://example3.com']))
