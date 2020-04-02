import sqlalchemy as sa
from databases import Database

from starlette_core.config import config

database = Database(config.database_url)
metadata = sa.MetaData()
