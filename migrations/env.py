import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from dotenv import load_dotenv

load_dotenv()
# ---------------------------------------------------------
# Path Setup:
# ---------------------------------------------------------
# Find the directory of the current file (env.py)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Path to the app folder containing models (adjust if needed)
APP_DIR = os.path.abspath(os.path.join(BASE_DIR, '../backend/src/models'))

# Include APP_DIR in Python's module search path
sys.path.append(APP_DIR)

# Import your SQLAlchemy Base where models are defined
from base import Model1Base as Base

# Load environment variables from the .env file


# Optional: Print directories for debugging
print(f"BASE_DIR: {BASE_DIR}")
print(f"APP_DIR: {APP_DIR}")
print(f"DATABASE_URL: {os.getenv('DATABASE_URL')}")
# ---------------------------------------------------------

# ---------------------------------------------------------
# Alembic Configuration:
# ---------------------------------------------------------
# Access the Alembic Config object to get values from alembic.ini
config = context.config

# Log file configuration, if necessary
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set metadata for autogeneration (use SQLAlchemy Base)
target_metadata = Base.metadata

# Set SQLAlchemy URL dynamically using the environment variable
config.set_main_option('sqlalchemy.url', os.getenv("DATABASE_URL"))


# ---------------------------------------------------------
# Migration Functions:
# ---------------------------------------------------------
def run_migrations_offline():
    """Run migrations in 'offline' mode without a DB connection."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode with a DB connection."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


# ---------------------------------------------------------
# Check Mode and Run:
# ---------------------------------------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()



