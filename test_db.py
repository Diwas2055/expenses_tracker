import databases
import sqlalchemy
import asyncio

from app.config.settings import get_settings

DATABASE_URL = (
    f"postgresql://{get_settings().db_user}:{get_settings().db_password}@"
    f"{get_settings().db_address}:{get_settings().db_port}/"
    f"{get_settings().db_name}"
)

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()


class DatabaseSession:
    def __init__(self, database):
        self.database = database

    async def __aenter__(self):
        await self.database.connect()
        return self.database

    async def __aexit__(self, exc_type, exc, tb):
        await self.database.disconnect()


async def get_database():
    """Return the database connection as an asynchronous context manager."""
    return DatabaseSession(database)


async def create_tables():
    async with await get_database() as db:
        """Create the database tables."""
        user_query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) NOT NULL UNIQUE,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            role VARCHAR(255) NOT NULL DEFAULT 'user',
            banned BOOLEAN NOT NULL DEFAULT FALSE,
            created_at TIMESTAMP NOT NULL DEFAULT NOW(),
            updated_at TIMESTAMP NOT NULL DEFAULT NOW()
        );
        """
        await db.execute(query=user_query)


async def main():
    await create_tables()


if __name__ == "__main__":
    asyncio.run(main())
