from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from src.commons.config import settings


class DBConnectionHandler:
    """Sqlalchemy database connection"""

    def __init__(self):
        self.__connection_string = f"{settings.db_url}"
        self.session = None

    def get_engine(self):
        """Return connection Engine
        :parram - None
        :return - engine connection to Database
        """
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        engine = self.get_engine()
        session_maker = sessionmaker(class_=Session)
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()  # pylint: disable=no-member
