from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from lib.db.database import Base, engine  # Import database and models
from lib.db.models import Task  # Import Task model

# Alembic configuration
config = context.config

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

# Add the models to Alembic's metadata
target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(url=engine.url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
