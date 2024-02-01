from pathlib import Path

from pydantic import Field
from pydjantic import BaseDBConfig

BASE_DIR = Path(__file__).resolve().parent.parent


class DatabaseSettings(BaseDBConfig):
    default: str = Field(
        default=str(f"sqlite:///{BASE_DIR}/db.sqlite3"),
        validation_alias="DATABASE_URL",
    )
