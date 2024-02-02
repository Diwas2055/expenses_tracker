# from app.queries.tables_queries import tables
from app.database.db import database_client

tables = ["users", "expenses", "incomes", "shared_amount"]


async def drop_all_tables():
    """Create the database tables."""
    async with await database_client() as db:
        try:
            for table in tables:
                await db.execute(f""" DROP TABLE IF EXISTS {table} CASCADE;""")
                print(f"Table {table} dropped.")
        except Exception as exc:
            print(f"Error dropping tables: {exc}")
            raise exc
    return True


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(drop_all_tables())
