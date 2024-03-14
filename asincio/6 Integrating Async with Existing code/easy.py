import asyncio
import requests

# Synchronous function that performs a blocking network request
def blocking_request():
    print("Starting blocking network request...")
    response = requests.get('http://example.com')
    print(f"Blocking request completed with response length: {len(response.text)}")

async def run_blocking_request():
    loop = asyncio.get_running_loop()
    # Run the blocking function in a default executor (ThreadPoolExecutor)
    await loop.run_in_executor(None, blocking_request)

if __name__ == '__main__':
    asyncio.run(run_blocking_request())
