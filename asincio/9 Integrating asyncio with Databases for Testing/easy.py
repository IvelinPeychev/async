import asyncio
from databases import Database

DATABASE_URL = 'sqlite:///./test.db'
GMAIL_USERS = 100

async def test_check_db_records():
    database = Database(DATABASE_URL)

    await database.connect()

    # Corrected SQL syntax for LIKE wildcard pattern
    query = 'SELECT * FROM users WHERE email LIKE :email'
    records = await database.fetch_all(query=query, values={"email": "%gmail.com"})

    assert len(records) == GMAIL_USERS, f"Expected {GMAIL_USERS}, got {len(records)} Gmail users."

    await database.disconnect()

if __name__ == '__main__':
    asyncio.run(test_check_db_records())

