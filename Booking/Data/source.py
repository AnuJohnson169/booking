
from sqlalchemy import create_engine
from API.Booking.Data.Models.Models import Base
from API.utils import parse_config

config = parse_config()

sqldb_uri = config.get('SQL', 'uri')


class SqlDB(object):
    """SqlDB Connection"""

    def __init__(self):
        try:
            self.engine = create_engine(sqldb_uri,echo=True)
            Base.metadata.create_all(self.engine)
        except Exception as ex:
            raise Exception(str(ex))