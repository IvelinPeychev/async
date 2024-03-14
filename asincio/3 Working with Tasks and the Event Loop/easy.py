import asyncio


async def foo():
    print('fetching web content...')
    await asyncio.sleep(4)
    print('fetching web content is completed')


async def foo2():
    print('processing data...')
    await asyncio.sleep(2)
    print('processing data is completed')

async def main():
    task1 = asyncio.create_task(foo())
    task2 = asyncio.create_task(foo2())
    await task1
    await task2


async def main2():
    await asyncio.gather(foo(), foo2())


if __name__ == '__main__':
    asyncio.run(main2())