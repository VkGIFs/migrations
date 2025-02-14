# noqa: E401
from alembic import context
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from src.settings import get_settings

config = context.config

Base = declarative_base()

def include_object(object, name, type_, reflected, compare_to):
    if type_ == "column" and object.info.get("skip_autogenerate", False):
        return False

    return True


def run_migrations_online() -> None:
    engine = create_engine(get_settings().DATABASE_URL)
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=Base.metadata,
            compare_type=True,
            include_object=include_object,
        )
        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()