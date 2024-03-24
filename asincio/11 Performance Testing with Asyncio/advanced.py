import asyncio
import aiohttp
import time

class StressTester:
    def __init__(self, url, num_clients, request_rate):
        self.url = url
        self.num_clients = num_clients
        self.request_rate = request_rate
        self.metrics = []

    async def _worker(self, session):
        while True:
            start_time = time.time()
            async with session.get(self.url) as response:
                await response.text()
                end_time = time.time()
                self.metrics.append(end_time - start_time)
            await asyncio.sleep(1 / self.request_rate)

    async def run(self):
        async with aiohttp.ClientSession() as session:
            workers = [asyncio.create_task(self._worker(session)) for _ in range(self.num_clients)]
            await asyncio.sleep(10)  # Run the test for a fixed duration
            for worker in workers:
                worker.cancel()
            await asyncio.gather(*workers, return_exceptions=True)

    def report(self):
        avg_response_time = sum(self.metrics) / len(self.metrics)
        print(f"Test completed with {len(self.metrics)} requests.")
        print(f"Average Response Time: {avg_response_time:.2f} seconds")

async def main():
    tester = StressTester(url="https://example.com", num_clients=50, request_rate=5)
    await tester.run()
    tester.report()

if __name__ == "__main__":
    asyncio.run(main())
