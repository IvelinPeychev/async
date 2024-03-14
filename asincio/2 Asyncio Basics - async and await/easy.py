import asyncio

async def foo(delay, name):
    await asyncio.sleep(delay)
    print(f'Hello {name}')


async def foo2():
    await foo(5, 'John')
    await foo(4, 'Jill')
    await foo(1, 'Glen')


if __name__ == '__main__':
    asyncio.run(foo2())
