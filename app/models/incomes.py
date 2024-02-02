from sqlalchemy import Column, DECIMAL, String, TIMESTAMP, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import text
from sqlalchemy.sql.schema import ForeignKey
from app.database.db import metadata

incomes = Table(
    "incomes",
    metadata,
    Column(
        "id",
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
    ),
    Column("user_id", UUID(as_uuid=True), ForeignKey("users.id")),
    Column("amount", DECIMAL(10, 2)),
    Column("description", String(255)),
    Column("created_at", TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")),
    Column("updated_at", TIMESTAMP, server_default=None),
)
