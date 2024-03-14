import aiofiles
import asyncio


async def foo(string):
    async with aiofiles.open('test.txt', 'w') as f:
        await f.write(string)

if __name__ == '__main__':
    asyncio.run(foo('test'))

    