import asyncio

async def foo():
    print('Download task has started')
    await asyncio.sleep(10)
    print('Download task has finished')

if __name__ == '__main__':
    asyncio.run(foo())