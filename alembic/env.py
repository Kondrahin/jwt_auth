import pathlib
import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

# init config
from app.settings.config import config

# If start not from docker
#sys.path.append(str(pathlib.Path(__file__).resolve().parents[3]))
sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))

from app.db.sqlalchemy import Base, make_url_sync  # isort:skip
import app.db.models  # isort:skip

postgres_dsn = make_url_sync(config.POSTGRES_DSN)
context_config = context.config
fileConfig(context_config.config_file_name)
target_metadata = Base.metadata
context_config.set_main_option("sqlalchemy.url", postgres_dsn)


def run_migrations_online() -> None:
    connectable = engine_from_config(
        context_config.get_section(context_config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    print(config.POSTGRES_DSN)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
