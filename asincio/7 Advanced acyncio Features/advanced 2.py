import asyncio
import random


# Simulate a long-running task
async def fetch_data(task_id):
    print(f"Task {task_id}: Fetching data...")
    # Random sleep to simulate variable task duration
    await asyncio.sleep(random.randint(2, 5))
    print(f"Task {task_id}: Data fetched successfully!")


async def main():
    tasks = [asyncio.create_task(fetch_data(i)) for i in range(5)]
    await asyncio.sleep(3)
    print('Stopping the tasks')

    for task in tasks:
        task.cancel()

    await asyncio.gather(*tasks, return_exceptions=True)

    # try:
    #     await asyncio.gather(*tasks)
    # except asyncio.CancelledError:
    #     print('Task was cancelled')

    for i, task in enumerate(tasks):
        if task.cancelled():
            print(f'Task {i} cancelled')
        elif task.done():
            print(f'Task {i} is bombastic')



if __name__ == "__main__":
    asyncio.run(main())