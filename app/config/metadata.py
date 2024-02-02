"""This file contains Custom Metadata for your API Project.

Be aware, this will be re-generated any time you run the
'api-admin custom metadata' command!
"""
from app.config.helpers import MetadataBase

custom_metadata = MetadataBase(
    title="Expense Tracker API",
    description="This is a FastAPI template for building API's.",
    repository="",
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
    contact={
        "name": "Diwash Bhandari",
        # "url": "https://www.gnramsay.com",
    },
    email="diwasb54@gmail.com",
    year="2024",
)
