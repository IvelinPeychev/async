import asyncio
import time


async def foo(filename):
    print(f'Download task has started for {filename}')
    await asyncio.sleep(10)
    print(f'Download task has finished for {filename}')


async def foo2():
    start_time = time.perf_counter()
    await asyncio.gather(
        foo('filename1'),
        foo('filename2'),
        foo('filename3')
    )
    end_time = time.perf_counter()
    print(f'Download task took {end_time - start_time} seconds')

if __name__ == '__main__':
    asyncio.run(foo2())