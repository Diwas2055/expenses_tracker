"""Control the app settings, including reading from a .env file."""
import sys
from functools import lru_cache

from pydantic import BaseSettings

try:
    from .metadata import custom_metadata
except ModuleNotFoundError:  # pragma: no cover
    from custom_helpers.metadata import metadata_init

    metadata_init()
    print("INFO:     Custom Metadata file created. Please edit and re-run.")
    sys.exit(1)


class Settings(BaseSettings):
    """Main Settings class.

    This allows to set some defaults, that can be overwritten from the .env
    file if it exists.
    Do NOT put passwords and similar in here, use the .env file instead, it will
    not be stored in the Git repository.
    """

    base_url: str = "http://localhost:8000"

    cors_origins: str = "*"

    # Setup the Postgresql database.
    db_user: str = "my_db_username"
    db_password: str = "Sup3rS3cr3tP455w0rd"
    db_address: str = "localhost"
    db_port: str = "5432"
    db_name: str = "api-template"

    # Setup the TEST Postgresql database.
    test_db_user: str = "my_db_username"
    test_db_password: str = "Sup3rS3cr3tP455w0rd"
    test_db_address: str = "localhost"
    test_db_port: str = "5432"
    test_db_name: str = "api-template-test"

    # JTW secret Key
    secret_key: str = "32DigitsofSecretNembers"
    access_token_expire_minutes: int = 120

    # Custom Metadata
    api_title: str = custom_metadata.title
    api_description: str = custom_metadata.description
    repository: str = custom_metadata.repository
    contact: dict = custom_metadata.contact
    license_info: dict = custom_metadata.license_info
    year: str = custom_metadata.year

    # email settings
    mail_username: str = "test_username"
    mail_password: str = "s3cr3tma1lp@ssw0rd"
    mail_from: str = "test@email.com"
    mail_port: str = 587
    mail_server: str = "mail.server.com"
    mail_from_name: str = "FASTAPI Template"
    mail_starttls: str = True
    mail_ssl_tls: str = False
    mail_use_credentials: str = True
    mail_validate_certs: str = True

    class Config:
        """Override the default variables from an .env file, if it exists."""

        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    """Return the current settings."""
    return Settings()
