import asyncio


async def foo1():
    print('Download started')
    await asyncio.sleep(12)
    print('Download finished')

async def foo2():
    print('Input started')
    await asyncio.sleep(4)
    print('Input finished')

async def foo3():
    print('Film started')
    await asyncio.sleep(10)
    print('Film finished')


async def main():
    await asyncio.gather(foo1(), foo2(), foo3())

if __name__ == '__main__':
    asyncio.run(main())