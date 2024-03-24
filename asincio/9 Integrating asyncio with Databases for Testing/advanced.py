import asyncio
from databases import Database

DATABASE_URL = 'sqlite:///./test.db'
TEST_USER = 'test_user_account'

async def test_multi_operations():
    database = Database(DATABASE_URL)

    await database.connect()

    # Start a transaction
    transaction = await database.transaction()
    try:
        # Create user in table users
        query = 'INSERT INTO users(name) VALUES(:name)'
        await database.execute(query=query, values={'name': TEST_USER})

        # Check if the user is created
        query = 'SELECT * FROM users WHERE name = :name'
        user = await database.fetch_one(query=query, values={'name': TEST_USER})
        assert user['name'] == TEST_USER, f'User with name {TEST_USER} does not exist'

        # Delete the user from DB
        query = 'DELETE FROM users WHERE name = :name'
        await database.execute(query=query, values={'name': TEST_USER})
        user = await database.fetch_one(query=query, values={'name': TEST_USER})
        assert user is None, f'User {TEST_USER} is still present in the database'
    except AssertionError as e:
        # Rollback in case of assertion error
        await transaction.rollback()
        raise
    else:
        # Commit if all is good
        await transaction.commit()
    finally:
        # Cleanup
        await database.disconnect()

if __name__ == "__main__":
    asyncio.run(test_multi_operations())

