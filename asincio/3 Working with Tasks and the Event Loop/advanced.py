import asyncio

async def foo(number, seconds):
    print(f'Task has {number} started')
    await asyncio.sleep(seconds)
    print(f'Task has {number} finished')


async def main(n, s):
    tasks = []
    for i in range(1, n+1):
        task = asyncio.create_task(foo(i, s))
        tasks.append(task)

    await asyncio.gather(*tasks) # passing the arguments to the gather function

if __name__ == '__main__':
    asyncio.run(main(50, 3))

