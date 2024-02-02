"""Setup the Database and support functions.."""
import databases
import sqlalchemy

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


async def database_client():
    """Return the database connection as an asynchronous context manager."""
    return DatabaseSession(database)


async def get_database():
    async with await database_client() as db:
        yield db
