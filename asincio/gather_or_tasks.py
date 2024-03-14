import asyncio


async def fetch_user_data(user_id):
    # Simulates fetching data
    print(f"Fetching data for user {user_id}...")
    await asyncio.sleep(7-user_id)  # Simulates delay in fetching data
    print(f"Fetched data for user {user_id}.")
    return user_id, f"data_{user_id}"  # Return both user_id and data


async def process_user_data(user_id, data):
    # Simulates processing data
    print(f"Processing data for user {user_id}: {data}...")
    await asyncio.sleep(3)  # Simulates delay in processing data
    print(f"Processed data for user {user_id}.")


async def main():
    # Create tasks for fetching data
    tasks = [asyncio.create_task(fetch_user_data(user_id)) for user_id in range(1, 3)]

    # Wait for each fetch task to complete and then start processing immediately
    for task in asyncio.as_completed(tasks):
        user_id, data = await task  # Await the task directly to get its result
        await process_user_data(user_id, data)



async def main2():
    data1 = await fetch_user_data(1)
    data2 = await fetch_user_data(2)
    await asyncio.gather(process_user_data(1, data1), process_user_data(2, data2))



if __name__ == '__main__':
    asyncio.run(main())