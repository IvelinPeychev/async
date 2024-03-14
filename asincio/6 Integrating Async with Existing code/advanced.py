import asyncio
import aiohttp
import requests
import time


# Define the synchronous version of the requests
def sync_get_request(url):
    print(f"Starting synchronous request to {url}")
    response = requests.get(url)
    print(f"Completed synchronous request to {url} with response length: {len(response.text)}")


def sync_main():
    urls = ['http://example.com', 'https://www.python.org', 'https://httpbin.org/get']
    start_time = time.time()
    for url in urls:
        sync_get_request(url)
    end_time = time.time()
    print(f"All synchronous requests completed in {end_time - start_time:.2f} seconds.")


# Define the asynchronous version of the requests
async def async_request(url):
    print("Starting async request...")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response_text = await response.text()
            print(f"Async request completed with response length: {len(response_text)}")


async def async_main():
    start_time = time.time()
    urls = ['http://example.com', 'https://www.python.org', 'https://httpbin.org/get']
    await asyncio.gather(*(async_request(url) for url in urls))
    end_time = time.time()
    print(f"All asynchronous requests completed in {end_time - start_time:.2f} seconds.")


# Execute synchronous and asynchronous mains separately
if __name__ == '__main__':
    print("Running synchronous version:")
    sync_main()

    print("\nRunning asynchronous version:")
    asyncio.run(async_main())

