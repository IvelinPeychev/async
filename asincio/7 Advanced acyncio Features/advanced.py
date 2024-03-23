import asyncio
import random


# Simulate a long-running task
async def fetch_data(task_id):
    print(f"Task {task_id}: Fetching data...")
    # Random sleep to simulate variable task duration
    await asyncio.sleep(random.randint(2, 5))
    print(f"Task {task_id}: Data fetched successfully!")


# Create and manage tasks
async def main():
    # Create a list of tasks
    tasks = [asyncio.create_task(fetch_data(i)) for i in range(5)]

    # Simulate running for a few seconds then cancelling tasks
    await asyncio.sleep(3)  # Let tasks run for 3 seconds
    print("Cancelling tasks...")

    # Cancel all tasks
    for task in tasks:
        task.cancel()

    # Attempt to gather cancelled tasks and handle CancelledError
    try:
        await asyncio.gather(*tasks)
    except asyncio.CancelledError:
        print("Tasks were cancelled.")

    # Optionally, you can check if tasks were indeed cancelled
    for i, task in enumerate(tasks):
        if task.cancelled():
            print(f"Task {i} was cancelled.")
        elif task.done():
            # Task completed before cancellation request
            print(f"Task {i} completed before cancellation.")


asyncio.run(main())