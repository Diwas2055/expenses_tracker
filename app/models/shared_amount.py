from sqlalchemy import Column, DECIMAL, ForeignKey, String, TIMESTAMP, Table, text
from sqlalchemy.dialects.postgresql import UUID
from app.database.db import metadata

shared_amount = Table(
    "shared_amount",
    metadata,
    Column(
        "id",
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
    ),
    Column("user_id", UUID(as_uuid=True), ForeignKey("users.id")),
    Column("amount", DECIMAL(10, 2)),
    Column("share_user", String(255)),
    Column("created_at", TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")),
    Column("updated_at", TIMESTAMP, server_default=None),
)
