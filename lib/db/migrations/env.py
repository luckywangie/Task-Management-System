from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context
import os

# This is the Alembic Config object, which provides access to values within the .ini file
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Explicitly get the database URL from alembic.ini OR use a default fallback
db_url = config.get_main_option("sqlalchemy.url") or "sqlite:///lib/db/database.db"

# Import your models here to ensure Alembic can detect them for autogeneration
from lib.db.models import Base  # Adjust this import based on your project structure

# Target metadata for 'autogenerate' support
target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=db_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = create_engine(db_url, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
