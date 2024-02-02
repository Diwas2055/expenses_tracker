from sqlalchemy import TIMESTAMP, Boolean, Column, Enum, String, Table, text
from sqlalchemy.dialects.postgresql import UUID
from app.database.db import metadata
from app.models.enums import RoleType

User = Table(
    "users",
    metadata,
    Column(
        "id",
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
    ),
    Column("email", String(120), unique=True),
    Column("password", String(255)),
    Column("first_name", String(30)),
    Column("last_name", String(50)),
    Column(
        "role",
        Enum(RoleType),
        nullable=False,
        server_default=RoleType.user.name,
    ),
    Column("banned", Boolean, default=False),
    Column("verified", Boolean, default=False),
    Column("created_at", TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")),
    Column("updated_at", TIMESTAMP, server_default=None),
)
