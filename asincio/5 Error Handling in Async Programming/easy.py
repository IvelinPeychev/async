import asyncio
import random


async def foo():
    i = random.randint(1, 5)
    try:
        print('Starting the process')
        if i == 3:
            raise ValueError(f"The number error is raised for {i}")
        else:
            print(f'The task for {i} is Ok')
            print('Process ended')
    except ValueError as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    asyncio.run(foo())