import asyncio
import aiohttp
import time

async def fetch(session, url):
    start_time = time.time()
    async with session.get(url) as response:
        await response.text()
        end_time = time.time()
        return end_time - start_time

async def load_test(url, num_requests):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for _ in range(num_requests)]
        response_times = await asyncio.gather(*tasks)
        return response_times

async def main():
    url = "https://example.com"
    num_requests = 100
    response_times = await load_test(url, num_requests)
    avg_response_time = sum(response_times) / len(response_times)
    print(f"Average Response Time: {avg_response_time:.2f} seconds")
    assert avg_response_time < 1, "Average response time exceeded 1 second."

if __name__ == "__main__":
    asyncio.run(main())
