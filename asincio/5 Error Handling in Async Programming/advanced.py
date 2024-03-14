import asyncio
import random


async def foo():
    i = random.randint(1, 5)
    if i == 3:
        raise ValueError(f"The number error is raised for {i}")
    else:
        return f'The task for {i} is Ok'


async def foo2():
    tasks = [asyncio.create_task(foo()) for i in range(1, 10)]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for result in results:
        if isinstance(result, Exception):
            print(f'Caught an exception: {result}')
        else:
            print(f'Got task result: {result}')

if __name__ == '__main__':
    asyncio.run(foo2())