# pylint: disable=too-few-public-methods
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import VARCHAR

from src.models import BaseDatetimeModel


class UserModel(BaseDatetimeModel):
    """Model for users"""

    __tablename__ = "users"

    telegram_id = Column("telegram_id", VARCHAR(12), nullable=False)
    vk_access_token = Column("vk_access_token", VARCHAR(128), nullable=True)
